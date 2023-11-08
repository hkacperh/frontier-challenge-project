# frontier-challenge-project
HackUTD Frontier challenge project
Contributors: Hassan Hashemian, Syed Naqvi, Alveena Rahman

**UPDATE**: This project won 1st place for Frontier's challenge at HackUTD as well as the beginner track award for HackUTD overall.
This project is unfinished and could use more, but the repository has been archived to preserve its state when submitted for HackUTD.

This project involved a multifaceted solution to predict when Frontier internet networks would fail.

Using the Python-based sci-kit learn, we trained an ML model on network data offered by Frontier to predict when networks would fail.
To start off, we performed a weighted linear regression to reduce the number of components that went into training the model to the
core information that is likely  to affect whether a network would fail or not. Since nearly 99% of networks in the data set were not
failed, we had to make sure that our data was not overfitted. Thus, the model was trained repeatedly on data sets which involved failed
networks and successful networks. This left us with a model that had an accuracy of about 67-70% when predicting from a dataset with
many failures, and much higher when the dataset was normal (when it is nearly all successes).

To visualize how this model would be used to provide valuable information to Frontier, we created a basic website. Since the ML model
was trained with Python, we opted for a Python-based backend using Django. To provide robust frontend capabilities, we integrated
Vue.js into Django's existing frontend templates. To store network information, we set up a PostgreSQL database that stored basic
network information as well as their status: at no risk of failure (as predicted by the model), at risk of failure (as predicted by
the model), and confirmed to be at risked (when double checked by an administrator). We set up a basic API with our Django backend to
query this database to provide the quantity of networks in each of these categories as well as a list of the networks that fall under
the "at risk" and "confirmed risk" categories. With this, we made a basic page that displayed these statistics.

With more time, we would like to have connected the ML model to the website through more API endpoints. We also would have liked to 
make the frontend more robust, providing visualizations of the data as well as an analysis of common problems that lead to predicted
network failures.
