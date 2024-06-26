
from prompt_toolkit.formatted_text import FormattedText
from abc import ABC, abstractmethod
from event_system.events import add_item, remove_item, search_database
from cli.state_machine_global import GlobalState
from event_system.events import update_item
from items import item_factory, items


"""
Abstract baseclass for all states in the CLI statemachine. 
A state performs a function through its state_action() method.
It also contains information related to functionality in the CLI,
such as the text above the prompt (prompt_header), a list of autocompletions,
displaying the function of the escape key (escape_key_func) and a string that
is evaluated just before the prompt is rendered.
(perhaps the information should be abstracted to its own dataclass?)
"""
class StateABS(ABC):
    
    @abstractmethod
    def __init__(
            self, 
            prompt_header: str, 
            autocompletions: list[str] = [],
            escape_key_func = "return to main menu",
            pre_run = "self.prompt_session.default_buffer.start_completion",
        ) -> None:
        self._prompt_header = prompt_header
        self._autocompletions = autocompletions
        self._escape_key_func = escape_key_func
        
        # passed to an eval() inside the pre_run of a prompt-session
        self._pre_run = pre_run

    @property
    def prompt_header(self):
        return self._prompt_header

    @prompt_header.setter
    def prompt_header(self, value):
        self._prompt_header = value

    @property
    def autocompletions(self):
        return self._autocompletions
    
    @property
    def escape_key_func(self):
        return self._escape_key_func

    @property
    def pre_run(self):
        return self._pre_run

    @abstractmethod
    def state_action(self, user_input: str):
        pass
    
    
    def format_header(self) -> FormattedText:
        return FormattedText([
            ("#00BFFF",f"{self.prompt_header}")
        ])   
    
    def format_escape_key_func(self) -> FormattedText:
        return FormattedText([
            ("#495969", "Press "),
            ("#495969 italic", "escape "),
            ("#495969", f"to {self.escape_key_func}"),
        ])

class MainMenu(StateABS):
    def __init__(self) -> None:
        super().__init__(
            prompt_header="Main menu:",
            autocompletions=["Search", "Add new item"],
            escape_key_func = "exit the application",
        )
        
    def state_action(self, user_input: str) -> StateABS:
        match user_input:
            case "Search":
                return ChooseFieldToSearchBy()
            case "Add new item" | "Add":
                return AddNewItem()
            case _:
                print(f"input {user_input} not recognized")
                return self
        
class ChooseFieldToSearchBy(StateABS):
    
    field_names = ["Name", "Category", "Price", "Count"]
    
    def __init__(self) -> None:
        super().__init__(
            prompt_header="Field to search by?",
            autocompletions=self.field_names
        )
        
    def state_action(self, user_input: str):
        if self.field_names.__contains__( user_input.capitalize() ):
            return SearchByField(field_name=user_input)
        else:
            print(f"{user_input} is not a valid field name")
            return self        
            
class SearchByField(StateABS):
    
    def __init__(self, field_name: str) -> None:
        super().__init__(
            prompt_header=f"Search products by {field_name}",
        )
        self.field_name = field_name
    
    def state_action(self, user_input: str) -> StateABS:
        search_database.SearchDatabaseRequest(
            search_str=user_input, 
            field=self.field_name
            ).post()
        if GlobalState().last_search.__len__() == 0:
            return self
        else:
            return SelectItemFromSearch()
        
class AddNewItem(StateABS):
    
    field_names = ["Name", "Category", "Price", "Count"]
    
    def __init__(self, item_info: dict = {}) -> None:
        super().__init__(
            prompt_header="Adding new Item. Pick field to set",
            autocompletions=self.field_names,
        )
        self._item_info: dict = item_info
        print(item_info)
        self.when_all_fields_have_values()
        
    def when_all_fields_have_values(self):
        for field_name in self.field_names:
            if self._item_info.__contains__(field_name) == False:
                return
        self.autocompletions.extend(["Confirm Add"])
        self.prompt_header = "Confirm add, or edit info:"
        
    def state_action(self, user_input: str) -> StateABS:
        if user_input == "Confirm Add":
            try:
                item = item_factory.WarehouseItemFactory.create_new_item_from_dict(self._item_info)
                add_item.AddItemRequest(item).post()
                return MainMenu()
            except Exception as e:
                print("Item info not valid", e)
                return self
        if self.autocompletions.__contains__(user_input.capitalize()):
            return InputFieldValue(field_name=user_input, item_info=self._item_info)
        else:
            print(f"{user_input} is not a valid field, try again or return")
            return self

class InputFieldValue(StateABS):
    def __init__(self, field_name: str, item_info: dict = {}) -> None:
        super().__init__(
            prompt_header=f"Input {field_name}:",
        )
        self._field_name = field_name
        self._item_info = item_info

        
    def state_action(self, user_input: str) -> StateABS:
        validated = self.validate_field_value(user_input)
        if validated[0] == True:
            self._item_info[self._field_name] = validated[1]
            return AddNewItem(item_info=self._item_info)
        else:
            print(f"{user_input} is not valid for field {self._field_name}")
            return self
    
    def validate_field_value(self, value: str) -> tuple[bool, str|int|float]:
        try:
            validation = {
                "Name": lambda x: (True, str(x)),
                "Category": lambda x: (True, str(x)),
                "Price": lambda x: (float(x)>=0, float(x)),
                "Count": lambda x: (int(x)>=0, int(x)),            
            }
            return validation[self._field_name](value)
        except:
            return (False, value)

class SelectItemFromSearch(StateABS):
    def __init__(self) -> None:
        super().__init__(
            prompt_header="Select an item to interact with",
            autocompletions=GlobalState().get_names_in_last_search()
        )
    
    def state_action(self, user_input: str) -> StateABS:
        try:
            item = GlobalState().get_item_in_last_search(user_input)
            GlobalState().set_active_item_edit(item)
            return ChooseRemoveOrUpdate()
        except:
            print(f"{user_input} not recognized, try again or return")
            return self
        
class ChooseRemoveOrUpdate(StateABS):
    def __init__(self) -> None:
        super().__init__(
            prompt_header="What do you want to do?",
            autocompletions=["Remove", "Update"]                
        )
        
    def state_action(self, user_input: str) -> StateABS:
        match user_input.capitalize():
            case "Remove":
                return ConfirmRemove()
            case "Update":
                return ChooseFieldToUpdate()
            case _:
                print(f"{user_input} not recognized, try again or return")
                return self

class ConfirmRemove(StateABS):
    def __init__(self) -> None:
        super().__init__(
            prompt_header="Remove",
            autocompletions=["Yes", "No"]
        )
        
    def state_action(self, user_input: str) -> StateABS:
        match user_input.capitalize():
            case "Yes":
                remove_item.RemoveItemRequest(
                    GlobalState().get_active_item_edit() 
                ).post()
                return SelectItemFromSearch()
            case "No":
                return ChooseRemoveOrUpdate()
            case _:
                print(f"{user_input} not recognized, try again or return")
                return self
    
class ChooseFieldToUpdate(StateABS):
    def __init__(self) -> None:
        super().__init__(
            prompt_header="Update which field?",
            autocompletions=["Name", "Category", "Price", "Count"]
        )
        
    def state_action(self, user_input: str) -> StateABS:
        if self.autocompletions.__contains__(user_input.capitalize()):
            return UpdateField(user_input)
        else:
            print(f"{user_input} is not a valid field, try again or return")
            return self

class UpdateField(StateABS):
    def __init__(self, field_name: str) -> None:
        super().__init__(
            prompt_header=f"Input new {field_name}",
            
        )
        self._field_name = field_name
    
    def state_action(self, user_input: str) -> StateABS:
        validated = self.validate_field_value(user_input)
        if validated[0] == True:
            item = GlobalState().get_active_item_edit()
            update_item.UpdateItemRequest(
                item=item,
                update_field=self._field_name,
                new_value=validated[1],
            ).post()
            return ChooseFieldToUpdate()
        else:
            print(f"{user_input} is not valid for field {self._field_name}")
            return self
        
    
    # Try to cast user_input to correct type for the field,
    # and check if price/count is lower than 0. 
    def validate_field_value(self, value: str) -> tuple[bool, str|int|float]:
        try:
            validation = {
                "Name": lambda x: (True, str(x)),
                "Category": lambda x: (True, str(x)),
                "Price": lambda x: (float(x)>=0, float(x)),
                "Count": lambda x: (int(x)>=0, int(x)),            
            }
            return validation[self._field_name](value)
        except:
            return (False, value)    