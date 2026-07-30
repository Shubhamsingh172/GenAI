#day2
#venv 
# venv stands for virtual environment. It is a tool that helps to keep dependencies required by different projects in separate places, by creating virtual Python environments for them. This is one of the most important tools that most of the Python developers use.
# example : gta 5 and gta 6 are two different games, they have different requirements and dependencies. If you install them in the same environment, it may cause conflicts and errors. By using virtual environments, you can create separate environments for each project, ensuring that they have their own dependencies and do not interfere with each other.
# driver 2.0 and driver 3.0 are two different versions of the same game, they have different requirements and dependencies. If you install them in the same environment, it may cause conflicts and errors. By using virtual environments, you can create separate environments for each project, ensuring that they have their own dependencies and do not interfere with each other.
# hum log laptop ke actual environment kisi bhi particular driver ko which may lead to conflicts and errors. By using virtual environments, you can create separate environments for each project, ensuring that they have their own dependencies and do not interfere with each other.
# for each praticular week 1 and week 2 we have different requirements and dependencies. If you install them in the same environment, it may cause conflicts and errors. By using virtual environments, you can create separate environments for each project, ensuring that they have their own dependencies and do not interfere with each other.

#llm call or llm ka api call.
#Requirement of LLM call is to get the response from the model
#1. API Key banana padta hai. (API key is required to access the model)
#2 Client banate hai and ye client koi aur nhi hum hai.
#3. Next we need model which means every model has its own name and we have to specify the model name which we want to use.
#4. Message me hum kya bolna chahte hai wo specify karte hai. (Message is the input we want to give to the model)
#5. Message me do cheez hoti hai role and content. Role is the user or assistant and content is the actual message we want to give to the model.
#6. Role is the user or assistant and content is the actual message we want to give to the model. it has three type of role user, assistant and system. User is the person who is asking the question, assistant is the model which is giving the response and system is the model which is giving the response.
#7. User Role example 1)Whois is Virat Kohli? 2)What is the capital of India? 3)What is the population of India? ye message user ke dwara bheja gaya hai. Assistant Role example 1)Virat Kohli is an Indian cricketer and former captain of the Indian national team. 2)The capital of India is New Delhi. 3)The population of India is approximately 1.38 billion. ye message assistant ke dwara bheja gaya hai. System Role example 1)You are a helpful assistant. 2)You are a knowledgeable assistant. 3)You are a friendly assistant. ye message system ke dwara bheja gaya hai.
#8. koi bhi llm apna poora message yaad karke rakhta hai role and message and isko hum isko context bolte hai. Context is the information that the model has about the conversation. It helps the model to understand the conversation and give better responses.
#9. LLM ka response me do cheez hoti hai role and content. Role is the user or assistant and content is the actual message we want to give to the model. Role is the user or assistant and content is the actual message we want to give to the model. it has three type of role user, assistant and system. User is the person who is asking the question, assistant is the model which is giving the response and system is the model which is giving the response.
#example me jab bolte hai chatgpt ko your code is wrong toh usko kaise pata chalta hai konsa code because usko role and content ke dwara pata chalta hai. Role is the user or assistant and content is the actual message we want to give to the model. Role is the user or assistant and content is the actual message we want to give to the model. it has three type of role user, assistant and system. User is the person who is asking the question, assistant is the model which is giving the response and system is the model which is giving the response.
#10. System role ka matlab kya hota hai suppose hamara interview and we say to chatgpt give me in the one line answer toh hum log usko bolte hai you are an interviewer means usko aligned kar dete hai toh isi prakar ke prompt me jab hum uska role pehle se hi decide kar dete hai toh woh ek system ke jaisa behave karta hai and hum isko hi system role bolte hai. System role ka matlab hota hai ki hum log model ko ek particular role me set kar dete hai jisse ki woh uske according behave kare.
#Now Response kaise aata hai llm ke taraf se choices and usage. choices is nothing but the array of answer means kabhi kabhi chatgpt hume 2 prakar ke answer deta hai toh woh choices me aata hai. Usage is nothing but the number of tokens used in the conversation. Tokens are nothing but the number of words used in the conversation. For example, if we say "Hello" to the model, it will use 1 token. If we say "Hello, how are you?" to the model, it will use 5 tokens.
#har ek message me certain tokens kharch hota hai means jitna bada message utna token kharch hoga.

#code 
# import os 
# from pathlib import Path

# from django.test import client
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()  # Load environment variables from .env file
# myapi_key = os.getenv("GROQ_API_KEY")  # Get the API key from environment variables   
# if not myapi_key:
#     raise ValueError("GROQ_API_KEY is not set in the environment variables or api error.")

# client = Groq(api_key=myapi_key)  # Create a client instance with the API key and client bana diya
# model = "llama-3.3-70b-versatile"  # Specify the model to use and model bana diya
# role = "user"  # Specify the role for the message and role bana diya
# prompt = "What is the capital of India?"  # The message to send to the model and ek prompt likh diya
# message = {"role": role, 
#             "prompt": prompt}  
# # Create the message structure list of message means bahto saare message agar ek bhi message bhi poochna hai na toh list bana ke hi poochna padega  
# messages = [message] #agar do message rehta then message1 and message2 ko list me daal ke hi poochna padega similarly for n message.
# response = client.chat.completions.create(model = model, messages = messages)  # Send the message to the model and get the response

#day3 
#System role and temperature
# example of system role is when we say to chatgpt "You are a helpful assistant" then chatgpt will behave like a helpful assistant and give us the answer accordingly. Similarly, when we say to chatgpt "You are a knowledgeable assistant" then chatgpt will behave like a knowledgeable assistant and give us the answer accordingly. Similarly, when we say to chatgpt "You are a friendly assistant" then chatgpt will behave like a friendly assistant and give us the answer accordingly.
# pratyush example of system role is when we say i love you to teacher then she will behave differently and the stringent action can be taken on us similarly when we say i love you to our gf then the response may be differ also when we i love you to our daughter then response may be different
# insan ka role kaisa hai ai ki bhasha me wo ho gya hamara system role and insan ki personality kaisi hai at the core wo hamara ho gya temperature. Temperature is nothing but the randomness of the response. For example, if we say to chatgpt "You are a helpful assistant" then chatgpt will behave like a helpful assistant and give us the answer accordingly. Similarly, when we say to chatgpt "You are a knowledgeable assistant" then chatgpt will behave like a knowledgeable assistant and give us the answer accordingly. Similarly, when we say to chatgpt "You are a friendly assistant" then chatgpt will behave like a friendly assistant and give us the answer accordingly.

#System Role
#System role llm ko batata hai tum kon ho means tumhara aur mera is chat me kya role hai?
# example role : system (llm ko bataya hai uska role abhi system jaisa hai agar hamne specify nhi kiya uska role and user ke taraf se koi message aata hai toh woh kaisa behave karega ye hum predict nhi kar skte hai isiliye agar hamne pehle specify kiya ki uska role kaisa rehne wala hai toh woh uske according behave karega and yahi hamara system role hota hai.)
# context : you are my office colleague and behave like that.
#role : user(by default means jab hum koi message bhejenge toh hamara role defined rehta hai.)
#context : i love you (ye hamne user ki taraf se bheja hai)

#but in the real world iska impact kya hai and iska real world me kya kam hai.
# for example ek company claude ka subscription kharidti hai aur wo ek ai agent banana chahti hai(ai agent means ek worker/ employee smjh lo)
# similarly cluade ka jo llm rahega hum uske system role ko real type company role/post assign kar skte hai ki claude no.1 tum junior developer ho toh tum us hisab se sochna, claude no.2 tum senior developer ho toh tum us hisab se sochna, claude no.3 tum hr ho to tum us hisab se sochna, claude no.4 tum manager ho toh tum us hisab se sochna toh ye hota hai real world impact system ka agar system role nhi hota toh ye possible nhi hota ki hum kisko kya role define kar rahe particular cheez ka kam karwane ke liye. and similarly hum uske temperature ko bhi define kar skte hai ki tumhara temperature 0.1 hai means tumhara response ka randomness 0.1
# Temperature ka matlab kya hota hai ki hum llm ki personality ko alter kar rahe hote hai, personality ko alter karne ka matlab hum jo api use kar rahe hai groq ka usme hum temperature [0 - 2] tak ka temperature pass kar skte hai. temperature 0 ka matlab wo safe play karega means thoda kam creativity karega jo deterministic answer dega jo nearest hai and predictable hai example(bacchi predicting sunday, monday then wo tuesday ko predict karegi) and temperature 2 ka matlab wo thoda zyada creativity karega means thoda unpredictable answer dega example(bacchi predicting sunday, monday then wo anday ko predict karegi jiska koi significance nhi hai but creativity dikhaya usne) and temperature 1 ka matlab wo thoda creativity karega means thoda unpredictable answer dega example(bacchi predicting sunday, monday then wo wednesday ko predict karegi).
# suppose hamne llm ko poocha ki food delivery app ka nam batao toh uska ek safe prediction ye ho gya khana khazana, mantu ka dhaba jo ki temp - 0 safe prediction hai iska unsafe prediction kya ho gya swiggy means iska khane se related koi matlab nhi hai similarly t = 0 ka matlab wo khane se related answer dega t = 1 wo predict karega zomato jo ki rhyme hai tomato ka similaryly temperature ke hisab se wo prediction karega 
# toh temperature ka matlab hota hai ki ye llmm ki personality ko enhance karta hai 
# also hum jab kisi llm ko message bhejte hai toh wo hame estimate answer nhi bhej raha hota hai instead wo prediction karta hai temperature ke hisab ses and hamne upar disucss kiya hi hai temperature kya hota hai and different temperature ka different creativity.
# Temperature randomness(jisko hum tabse creativity bol rahe hai) badhata hai llm ka so that wo predict kr ske suppose agar hum kisi doctor ke liye app bana rahe hai toh wo facts pe prediction karega and similarly agar hum kisi media company ke liye story teller ka app bana rahe hai toh us llm ko creative hona padega to write story based on use cases hum temp ko adjust kar rahe hote hai also different use case ke liye different temp ki degree chahiye hoti hai

#day4 on tokens 
# suppose ek thela hai uske upar usually hum jo sellers rehte hai wo ready format me chocalate, anda, aur maggie pehle se prepare karke rakhte hai so that agar koi thela pe aayega then he will serve, also ek alag insan ye bhi bol skta hai ki mujhe chocolate anda maggie bana ke do jo ki reality me exist karta nhi hai still seller kya karega usko bana ke dega combined dish is cheez ko common reusable words bolte hai jo tokens me use hota hai.
#  tokens aaya kaise and uski kyu zarurat padi
#llm stands for large language models means aam bolchal ke bhasha me baat kar skte hai. llm is also a computer program and kisi bhi conmputer ko koi language smjh me nhi aata hai like use 0 and 1 me kuch cheez smjha aayega like hello message ko number me convert karega and jo input message hai uske liye output number bhi generate karega and us output number ko natural language me convert kiya jata hai like any language.
'''
1.first method : har ek letter ko uske ascii value me convert karke input banao then us ascii number ke base pe ek input generate hoga jo ki bahot bada hoga for example hello is word ke liye kya hi input hota 7269767679 ye aisa input aata sif ek word ke liye similarly agar sentence jata toh uske liye kya large input hota which is unimaginable and isiliye ye wala method utna effective nhi tha jiske wajah se isko nhi liya gya use me because agar ye method use hota na then chatgpt me limit lag gyi hoti like 4 words hi ek baar me pooch skte hai nhi toh din ke 10 sentences 4 words ke, sochne wali baat hai hum jo chat 3000 line ke karte hai uske sath how could llm handle this toh ek idea ye bhi aaya ki hashing ka use kar skte hai like we can add the words of sentence and produce the input the as well as output.
2.Second method : words to numbers like har word ko ek number assign kar dete hai jaisi ki oxford dictionary me collectively six lakh words hai which is not big as such isiliye ye wala method use kiya jaa skta tha means hello ko 1 and there ko 2 apple ko 3 example ke liye and har space se new word identify hota then uske base pe ek input generate hoga then similarly answer ke liye same technique ka use karke output generate hota then usko again uske natural language me convert kar dete but isme bhi ek problem hai ki hum log oxford dictionary ke hisab se baat nhi karte jo ki ek deficiency hai like we say my name is shubham isme shubham mentioned nhi hai oxford me also log new word invent karte hai like gali, etc. similarly log oxford dictionary ke hisab se nhi baat karte also har new word ko hum log hamesha add nhi kar skte like zomato, yaha, pagal, etc. like ye sab nhi hai dictionary me also iska yahi matlab no. of words hum english me bana skte hai wo infinity hai means koi bhi alag alag words ko jod kar isiliye ye method utna kargar nhi tha because konsa user kya likhega hum predict hi nhi kar skte the isiliye word ko number me nhi convert kar skte.
3.third method : ab jaake aaya tokens ka concept(common reusable words) : toh isme kya hua chatgpt ya konsa bhi llm jo scientist bana rahe the unhone internet pe exist karte hue saare words ko store kiya which is common and gave it to chatgpt for identifying. Toh token ka matlab ye hota hai ki chatgpt ya konsa bhi llm us word ko kaise janta hai like common reusable words ko toh llm as single token treat karega but for any uncommon words llm usko parts me break karta hai like pratyushifaction toh ye koi general word nhi hai jiska kuch meaning hota ho but llm isko parts me break karega and uska token generate karga like Shubham likha chatgpt pe toh wo isko as a 3 token le raha hoga break karke but jab hum bangalore likhte hai toh chatgpt ko smjhega poore internet pe bangalore jyada baar aaya hai shubham se to ye ek common word hai toh wo usko as a single token read karega similarly kuch log bolte hai ki token ka matlab 4 words ye sahi nhi hai but iska real meaning kya hai agar koi bada word chatgpt ko pata hai toh usko as a single token read krega also koi chota word jo usko nhi pata hai toh usko break karke tokens me generate karega hum ye shubham and bangalore wale example me dekh sakte hai jaha pe chatgpt bangalore jo size wise shubham se bada hai wo usko as a single token lega similarly shubham jo chota hai wo usko 3 tokens(just for example) me break kar dega.
ek word ko chote chote parts me baat kar hum common known words me jab convert karte hai na usko tokenizing bolte hai and token me convert ho jane ke baad tab jaa ke usko number assign hota hai also hamne kai baar suna hoga ki koi bolta hai mera tokens khatam ho gya hai then usko again avail karne ke liye hame subscription purchase karna pdta hai then at that time comapny word wise nhi token wise charge karti hai man liye ek token ka ek rupya then for 3 token 3 rupya hoga hence on et...
similarly token word hi hota hai but wo sub part hota hai word ka jiska matlab chatgpt ko pata ho
4.token padhna kyu zaruri hai because words and letters unlimited ho skte hai isiliye, koi llm decide karega like chatgpt ki hum 1crore token nikalenge internet se and usi pe operate karenge similarly koi dusra llm kuch aur decide kar skta hai like 2cr token from internet to operate
5. jab hum koi prompt llm ko dete hai toh wo tokens me toot jata hai then wo input llm ke pass jata hai then jab woh llm output send karta hoga toh uska output bhi token me toot jata hai then ek prompt ka input and output ka cost input token plus output token ka summation hota hai 
example : prompt diya hamne uske liye humko 100 token laga then uska output waha se generate hua uske liye 200 token laga then overall dono ka 300 token ek prompt ke input and output ka laga that's all.
6.Also Suppose hum log agar kisi company me kam rahe honge toh humara boss bolega ki mujhe aisa ai agents design karna hai jiska token limit hona chahiye and ye calculate jo hota hai token ka wo variable ke dwara hota hai isiliye token ka limit ho jane par hamara input bhi nhi jaata hai aur na output generate hota hai and ye hum kai baar chatgpt pe aur alag alg llm models par face kiye hai.
7.input and response me 2 types ke token hote hai input token + output/completion token and iska summation = total tokens 
'''

#day5 on structured output (we will learn today about pydantic and json)
'''
1. ab aaj ke session ke baad hum log sikhenge that how can we make project also ek homework diya hai ai resume parser jo ki resume as input leke usko parse karke shortlisting mechanism perfom karega that whether the candidates fit or not also hum agar kisi company me kam karenge then hamara hr bolega ki ek ai agent bana ke do jo resume ko dekhega based on the job description because n number of resume ko padhne ke liye hr ke pass time nhi hai wo bhi job description ke basis pe kon fit ho raha hai ya nhi, also jab hum konse bhi company me kam karenge na toh jo ai agent hum banayenge na toh uska output kisi aur code me me use ho raha hoga like big llm code jisse wo decision le sake acche se also humne jo ai agent banaya hoga wo kitne baar bhi chal skta hai like 1 million, 1 billion kitni bhi baar uska koi idea nhi.
2.agar hamne apne ai agent ko as it is string format me chhod diya then bade llm ke code liye bahot hard ho jayega to take decision or produce the output becaue string parsing bahot hard hota hai becaue paragraph me se humko kuch selective cheez parse karni hoti hai and also code konse bhi language me ho skta hai cpp, java, js, etc. also string ko kyu parse karna hai because computer ko normal bhasha nhi smjhta hai jaisa human ko smjhta hai usko sirf 0 and 1 smjhta hai isiliye string parsing karna jaruri hai.
example : man lo hum log ek ai agent bana rahe hai customer complain ke liye jo hame email pe aata hai and hume isko parse karna hai ai agent ki madad and send karna hai kisi bade ai agent ko so that wo categorize kar sake ki jo customer complain email pe aai hai wo konse category me lie karti hai like electronic, mechanical, it, ya food ka complain ka etc., also customer jo complain likhega wo english language me likhega like "Hi i am having certain certain issue with my smartphone" and ye complain likh ke hamne email pe bhej diya and ye email id llm ke pass jayega as a prompt and ab ye llm ki zimmedari hai user ka data nikalna like naam, email, phone numbers, issue etc. and agar ye nikalna hota toh ye bahot easy hota hamare liye but jab llm answer dega toh ye ho skta hai ki wo answer hame normal na de wo hume additional cheeze bhi de skta hai based on their understanding and jab llm ne answer diya ki name : shubham, phone : xxx1234, email : abc@gmail.com, issue = electronics and yaha dekho ye output hame english language me aaya hai provided by our ai agent and hum isko as it is nhi bhej sakte dusre code ko because ye string mem hai hamne isko parse kiya hi nhi hai also is me grammer use ho raha is, am etc, jabki isko variable me bhi store kiya jaa skta tha but llm humko uske hisab se answer dega which is in the string format which will create hard task for big llm, toh humko ek algorithm likhna padega jo ki parsing karta hoga string me essential information nikalne ke liye and string me parsing karna bahot hard process hai because konsa word actual me info hai wo decide karna difficult hai aur string parse karna and information nikalna is one of the hardest thing in computer program today.
3. agar hamne aisa ai agent banaya jo string parse karne me hi time laga raha hai then it is not efficient log hame gali denge ki kya bana ke de diya hai isiliye string ka output as it is pass nhi kar skte hai isiliye humko structured output pass karna hoga jo cheez chahiye wahi cheez pass honi chahiye 
4. Isi structured output ke problem ko solve karne ke liye and structured karne ke liye cheezo ko json aaya tha json isiliye nhi aaya tha ki bas llm ki problem solve kare because jab llm nhi tha tabse json hai, because server ko ek dusre se baat karni hoti hai jo alag alag jagah located hai like america, delhi, bombay, etc. toh json format ko use karte hai communicate karne ke liye and agar data as it is string me pass ho gyi toh dikkat hogi server ko fetch karne me isiliye data ko json format me bheja jata hai and ye most use hone wala approach hai because json store the data on key value pairs. like name : {"name" : "Shubham", "email" : "abc@gmail.com"} isif format ko json format bolte hai like ye easy hoga llm and server ke liye to fetch the informatio, infact json ke multiple json extractor and libraray hote hai infact agar hamne kisi ko json file ka data diya then wo data.file.name se direct kisi ka bhi name nikal skta hai same for other information too like data.file.phone, data.file.email like int phone = data.file.phone and ye human ke liye bhi assan hota hai and computer ke liye bhi aasaan hota hai. json output is the structured output bolte hai and string ka jo rehta hai wo unstructured output hota hai.
5.isiliye hum log kya karenge hamare llm se jo bhi output aayega usko json format me convert kar denge as it is llm ke output ko nhi bhejenge toh ye hota hai ki kyu output structured hona chahiye. But karenge kaise so isi cheez ko resolve karne ke liye hum pydantic use karenge, pydantic library ye use karunga jisko hum bolenge hum ye particular cheez chhaiye and wo wahi cheez store karega 
6.pydantic ek tarika hota hai llm ke program ko batane ka ki humko ye particular cheez chahiye and hum bolte hai hume isi format ka json output dena 
from pydantic import BaseModel(base model is also a library) isiliye hume jo cheez chahiye hoti hai hum uska class bana lete hai like niche banaya hai
class Ticket(BaseModel): (class ka nam ticket isiliye because har complain hamare liye as a ticket hai and hum ticket wise dekhenge customers ke complain)
    name : str
    email : str
    category : str
upar name, email, category hamne isiliye liya hai ki particular ticket se hame kya chahiye particular information
iske baad hum ek schema banate hai and schema ka matlab ek framework hota hai ki humk aisa particular cheez chahiye

Schema = Ticket.model.json.schema() #means upar jo teen cheez ka information hai uska ek schema ban gaya
response.format = {
    "type" : "json_format"
}
message_system = {
    "role" : "system",
    "content" : system_prompt
    }
system_prompt = f"""return output in json format in json fomat matching this scchema {schema}"""

text  = "complain"
message = {
    "role" : "user"
    "content" : prompt
    }

messages = [message_system, message]

toh ye poora code llm ko kya bolega mujhe jo bhi output aaye wo json format me do following this schema.
'''

#day 6 mini project llm resume evaluator

#part1--> HR uploads a Job Description and hum log job description ko json format me convert kar denge like role, required skills, preferred skills, minimum experience, educational requirement, responsibilites, is prakar ka hum log ek jobd nam ka ek class banayenge and uska ek schema banayenge and uske baad ek system prompt likhenge ki wo ek expert hr hai and scan this jobd schema
#agla prompt hum kya likhenge ki analyse the following job description and store it in json object ab hum usse se kya karenge readable format me convert kar denge.
#part2--> agla part ye hai ki resume ka schema kaise banega like har bacche ka resume alag alag ho skta hai koi experience likhega toh koi nhi likhega koi project likhta hai toh koi nhi likhta toh har baccha alag alag ajeeb cheez likh skta hai isi ke liye hume generalized section bana denge so that ambiguity naa aye uske liye hum log multiple class bana denge 
'''
class Experience 
    company
    role
    duration
    description
    skills used
    
class Resume 
    name 
    email
    phone 
    total_experience_years
    skills = list of skills(because skills multiple ho skti hai)
    experiences = list of [Experience class ka]
    project = list of [str]
    certifications = list[str]

rersume_schema = Resume(resume class ki madad se ek resume schema bana lenge)

'''

#part3 : Read Resume like resume padhna kaise hai usually resume do format me hota hai pdf nhi toh docx which is also known as document dono ke liye python me libraris diya hai
#do function banayenge read_pdf(file path) nhi toh read_docx(file path) then wo ek string de dega 
# ab hum ek function banayenge read_Resume karke(filepath) ye bhi ek file path lega agar ye pdf hai toh pdf ka function call karenge, agar wo docx format hai toh document wala function call hoga
#agar kuch nhi hai format toh none return kar denge hum.

#part4: ab main kam hai resume ko dekhenge resumes wale folder me and hum kya karenge resume wale folder pe iterate karenge sabse pehle hum kya karenge file path nikal lenge then resume_text = me function call karenge read_resume so that hume uska file path mil jayega ab paresed resume ka function likhenge (resumetext) ye lo resume resume and iska output kar ke do and jo bhi skills schema me defined hai wahi dega ek baar ye kar lenge toh hamare pass json format hoga parsed resume ka ab bas match karwana hai
#part5: class MatchResult ye ek bana lenge jiska use karke hum ek score nikalenge score can be float or integer details : dict , ek final score ka function(job parsedresume) bna lenge and usko bolenge tum ek hr recruiter ho then isko compare karo then hume ek score de dena and details me hume uski matching skills, name, missing skills and overall ek score de dena ye ek json result pass karega so that result.score, result.details