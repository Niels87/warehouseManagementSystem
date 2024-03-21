from events import event_abs, search_database, add_item, remove_item, update_item

"""
Builds argument tuples for stored database procedure,
based on Request-event types.
"""
class ProcArgsBuilder(object):
    
    @staticmethod
    def get_args(request: event_abs.EventABS) -> tuple:
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
                return (req.item.id, req.update_field, req.new_value)
            case search_database.SearchDatabaseRequest:
                req: search_database.SearchDatabaseRequest = request
                return (req.search_str,)
            case _:
                print(f"Request type <{type(request)}> not handled by ProcArgsBuilder")
    
    @staticmethod
    def get_proc_name(request: event_abs.EventABS) -> tuple:
        match type(request):
            case add_item.AddItemRequest:
                return "add_item"
            case remove_item.RemoveItemRequest:
                return "remove_item"
            case update_item.UpdateItemRequest:
                return "update_item"
            case search_database.SearchDatabaseRequest:
                return "search_by_name"
            case _:
                print(f"Request type <{type(request)}> not handled by ProcArgsBuilder")