from event_system.events import update_item
from event_system.events import add_item, event_abs, remove_item, search_database

"""
Builds argument tuples for stored database procedure,
based on Request-event types.
"""
class ProcedureArgumentsBuilder(object):
    
    @staticmethod
    def get_arguments(request: event_abs.EventABS) -> tuple:
        match type(request):
            case add_item.AddItemRequest:
                req: add_item.AddItemRequest = request
                item = req.item
                return (item.name, item.category, item.price, item.count)
            case remove_item.RemoveItemRequest:
                req: remove_item.RemoveItemRequest = request
                item = req.item
                return (item.id,)
            case update_item.UpdateItemRequest:
                # might not work if new value is int (field is price/count)
                req: update_item.UpdateItemRequest = request
                item = req.item
                print(f"id: {req.item.id}, field: {req.update_field}, new_val: {req.new_value}")
                return (req.item.id, req.update_field, req.new_value)
            case search_database.SearchDatabaseRequest:
                req: search_database.SearchDatabaseRequest = request
                return (req.search_str, req.field, 0)
            case _:
                print(f"Request type <{type(request)}> not handled by ProcArgsBuilder")
    
    @staticmethod
    def get_procedure_name(request: event_abs.EventABS) -> tuple:
        match type(request):
            case add_item.AddItemRequest:
                return "add_item"
            case remove_item.RemoveItemRequest:
                return "remove_item"
            case update_item.UpdateItemRequest:
                return "update_item"
            case search_database.SearchDatabaseRequest:
                return "search"
            case _:
                print(f"Request type <{type(request)}> not handled by ProcArgsBuilder")