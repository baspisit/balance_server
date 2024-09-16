from balance import balancing
data = 'H2,O2|H2O,A'
reactants, products = data.split('|')
reactants = reactants.split(',')
products = products.split(',')
print (reactants)
print (products)
balancing(reactants, products)