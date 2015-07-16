try:
    from keras.models import Sequential
    from keras.layers.core import Dense
    from keras.layers.recurrent import JZS1
except ImportError:
    print('Keras is not installed, do not use mut1model')

from .kerashistorymodel import *

class MUT1Model(KerasHistoryModel):
    """ Associate values to sequences of observations using the MUT1 model discovered
        by Jozefowicz et al,  2015.
    """

    def __init__(self, nb_actions, history_length, hidden_neurons):
        super().__init__(nb_actions, history_length, hidden_neurons)

    def createKerasModel(self, state_size):
        """ Create an LSTM-based neural network
        """
        model = Sequential()
        model.add(JZS1(state_size, self.hidden_neurons, activation='tanh', inner_activation='tanh', truncate_gradient=self.history_length))
        model.add(Dense(self.hidden_neurons, self.nb_actions, activation='linear'))

        return model