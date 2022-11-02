fruits = ['Banana','Apple','Bad','Pineapple','Strawberry','Grape']
for fruit in fruits:
  if fruit == 'Bad':
    continue
  st.caption(fruit)
for fruit in fruits:
  if fruit == 'Bad':
    break
  st.caption(fruit)
st.caption('By Nadi Duno')