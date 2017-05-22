# Aprendizagem Supervisionada padrão - SupervisedDataSet
#   Conjunto de Entradas que tenha entradas e alvos.
from pybrain.datasets import SupervisedDataSet

# Atalho BuildNetwork
#   Essa chamada retorna uma rede que tem duas entradas, três oculto e um único
#   neurônio de saída.
#   Na camada oculta, é construída a função Sigmoide por padrão
from pybrain.tools.shortcuts import buildNetwork

# Para ajustar os parâmetros dos módulos na aprendizagem supervisionada usando
# backpropagation.
from pybrain.supervised import BackpropTrainer


ds = SupervisedDataSet(2, 1) # Suporta entradas bidimensionais e alvos dimensionais

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

for inpt, target in ds:
    print inpt, target

# buildNetwork(nº entradas, nº intermediária, nº saídas, bias)
net = buildNetwork(ds.indim, 4, ds.outdim, bias=True)

# Os trainers tomam um módulo e um conjunto de dados para treinar o módulo para ajustar os dados no conjunto de dados.
                                                                    #Trocar essas linhas para:
trainer = BackpropTrainer(net,ds, learningrate=0.01, momentum=0.99) # trainer = BackpropTrainer(net,ds)
for epoch in range(0, 3000):                                        # for epoch in range(0, 10000):
    training = trainer.train();
    print(training);
    if training < 0.001:
        break




#print "\nWeights: ", net.params
print "\n\n"

print '0,0->', net.activate([0,0])
print '0,1->', net.activate([0,1])
print '1,0->', net.activate([1,0])
print '1,1->', net.activate([2,1])
