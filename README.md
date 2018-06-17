# 2 Fast 2 Furious <img src="https://i.ytimg.com/vi/_sjzBa3kVQM/maxresdefault.jpg" height="40">
# 2 Fast 2 Furious
### StuyHacks June 2018 Repo
### Joshua Weiner, Bill Ni

## Background
In our project, we wanted to combine two things of growing importance in the field of tech. The first, machine learning: we aimed to create a personal assistant that could hold a coherent conversation, but could also learn to improve its knowledge (with the help of the user) when it encounters something unfamiliar. The second: personalized tech, our personal assistant is able to learn more about its users, but also can function as a useful helper when the user is experiencing anything from a crisis to hunger.

## Project
Jesse H. Cai is a bot that loves to talk. But be warned, Jesse CAN pick up on social cues. If you start giving Jesse 1-word answers, your chat will be dropped, so please don't treat him as such.
As is the way with hastily-programmed chat bots, sometimes the conversation can get a little odd. Other times, Jesse will ask for help in order to learn more about what kind of messages go where, and what is an appropriate response.
Jesse runs using '''Python''', '''Flask''', and '''JavaScript'''. 

## Social Benefit and Impact
It is our hope that Jesse can get a user the proper location and contact information of emergency services should the user request it. Right now, as is detailed later, this is only limited to the current location of the project (Gekko). However, in the future we hope to increase our use of APIs to not only cover more locations, but also offer map services and contact information for the nearest sources of help around the world. In the developing world where mobile phones have spread rapidly, this kid of application could be especially poignant.
Furthermore, we hope that Jesse one day will be able to highlight signs of depression in its users based on sent messages, and either contact a loved one (if the user is a minor) or the authorities depending on what the user sends.

## How it works
Jesse works by comparing your input to a massive and constantly expanding database of possible inputs and replying with a random appropriate response. It also looks to see if there are any keywords in your messages that can help it identify what response is necessary.

## Launch
This was our first experience learning javascript (in addition to it being our first hackathon), and we really grappled with learning the complexities of the language in order to create a functioning project. This, in combination with the use of flask, meant that it was unfortunately had for us to set up a webpage that allowed for more than just a static server. (We tried to use Heroku, but were not experienced enough with the platform to accomplish this in time.) Ergo, our project can be launched, but only from a locally hosted server (Those 405 Errors certainly are something else). We are happy to demonstrate that for you today!

## Goals for this project
<ul> <li>It was one of our aims during this project for the helper functions of Jesse to be able to access/be given the user's location to give better recommendations. Unfortunately, we did not have much time to do this successfully, and were only able to implement this using the location of Gekko. So in the future, create that ability for the user to update their location constantly and receive different locations</li>
</li>As stated earlier, we also want to give Jesse the ability to display maps for the user based on their location and request for information, services, or food recommendations.</li>
<li>Improve the learning of Jesse, to better be able to pick up conversation without as direct user input as we have now. </li>
<li>Publish our chatbot online (should be done soon) for the general public to use, hopefully develop it into an app for mobile devices as well </li> </ul>

## Accrued knowledge
<ul><li> We came into StuyHacks Spring 2018 not knowing much about Flask of JavaScript. After hours pouring over documentation describing callbacks, we are much more proficient now then we were 36 hours ago. </li>
<li> We definitely learned the feel of the crunch when programming an entire project with limited time to do so. Because of this, we learned a lot about having to rely on one another, and eachothers' skills, to tackle the many aspects of our project.</li>
<li> In the past, we had done some work of converting back-end Python processing to front-end display. That was nothing compared to what we had to do over the past day, and our merging of the back-end and front-end of our project is something we are very proud of. </li>
<li> We learned a lot about Flask both as a language to help mediate between our various scripts and front-end displays, but also as a tool to develop and hosts projects locally. </li>
<li> Finally, we learned that taking the time to teach a program colloquial speech is a long and arduous process. </li> </ul>

**Our instructions are as follows:** <ul>
  <li>Type away</li>
  <li>...and enjoy!</li>
