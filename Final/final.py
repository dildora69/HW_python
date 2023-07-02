import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore')


encoder_data = pd.DataFrame(encoder.fit_transform(data[['whoAmI']]).toarray())

final_data = data.join(encoder_data)


print(final_data)