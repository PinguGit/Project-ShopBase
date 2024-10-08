from Backend import getCommand

def getType(table, dictionary, check):
    match table:
        case "product":
            if check == 0:
                return
            return getCommand.getProducts(dictionary)
        case "hersteller":
            if check == 0:
                return
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
            if check == 0:
                return
            return getCommand.getCustomers(dictionary)
        case "verkauefer_produkte":
            return