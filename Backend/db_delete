def delete_by_obejct(obj):
    obj_type = type(obj).__name__

    match obj_type:
        case "product":
            table = "product"
        case "manufacturer":
            table = "hersteller"
        case "country":
            table = "laender"
        case "password":
            table = "passwort"
        case "location":
            table = "orte"
        case "vendor":
            table = "verkauefer"
        case "customer":
            table = "kunde"
    return(table)
    
