import streamlit as st
import joblib
model = joblib.load('Sentiment_Analyzer')
st.title('Sentiment Analyzer')
input = st.text_input('Enter your review:')
bad_reviews = ['bad','worse','worst','very bad','substandard','poor','inferior','second rate','second class','unsatisfactory'
                ,'inadequate','unacceptable','not up to scratch','not up to par','deficient','imperfect','defective','faulty'
                ,'shoddy','amateurish','careless','negligent','dreadful','awful','terrible','abominable','frightful','atrocious'
                ,'disgraceful','deplorable','hopeless','worthless','laughable','lamentable','miserable','sorry','thirdrate'
                ,'diabolical','execrable','incompetent','inept','inexpert','ineffectual','crummy','rotten','pathetic','useless'
                ,'woeful','bum','lousy','appalling','abysmal','pitiful','godawful','dire','not up to snuff','the pits','duff'
                ,'chronic','rubbish','pants','a load of pants','ropy','poxy','egregious','vulgar slangcrap','shit','chickenshit'
                ,'unpleasant','disagreeable','unwelcome','unfortunate','unfavourable','unlucky','adverse','nasty','terrible'
                ,'dreadful','awful','grim','distressing','regrettable']
for i in input.split():
  if i in bad_reviews:
    output = [['Negative']]
    break
  else:
    output = model.predict([input])
if st.button('Predict'):
  st.title(output[0])
