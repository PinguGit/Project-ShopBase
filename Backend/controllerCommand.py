import getCommand

def getType(table, dictionary):
    match table:
        case "product":
            return getCommand.getProducts(dictionary)
        case "hersteller":
            return getCommand.getManufacturers(dictionary)
        case "laender":
            return
        case "kundenbestellungen":
            return
        case "bestellung":
            return
        case "verkauefer":
            return
        case "passwort":
            return
        case "orte":
            return
        case "kunde":
            return getCommand.getCustomers(dictionary)
        case "verkauefer_produkte":
            return
        