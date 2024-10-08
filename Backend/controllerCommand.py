import getCommand

def getType(table, dictionary):
    match table:
        case "product":
            return getCommand.getProducts(dictionary)
        case "hersteller":
            return getCommand.getManufacturers(dictionary)
        case "laender":
            return 'Grenzen müssen Menschen weichen'
        case "kundenbestellungen":
            return 'fick dich'
        case "bestellung":
            return 'gibt nen anderen endpunkt hierführ du seniler Oppa'
        case "verkauefer":
            return getCommand.getVendors(dictionary)
        case "passwort":
            return 'hättest du wohl gerne'
        case "orte":
            return 'geht dich nix an'
        case "kunde":
            return getCommand.getCustomers(dictionary)
        case "verkauefer_produkte":
            return 'raff dich'
        