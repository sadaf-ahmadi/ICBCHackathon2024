import azure.functions as func
import logging
import json
from datetime import datetime

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="HttpIntegration")
def HttpIntegration(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    response = {
        "calls": [
            {
    "short": {
        "representativeName": "Bobby",
        "customerName": "Emily",
        "date": "04/22/2024",
        "callLength": 4,
        "summary": "This is a call summary",
        "transcription": [
            {
                "speaker": "Bobby",
                "text": "Hi, this is Bobby calling from ICBC's assembly."
            },
            {
                "speaker": "Bobby",
                "text": "Hi, this is Emily. Yes."
            },
            {
                "speaker": "Bobby",
                "text": "Oh, hi, Emily. I'm glad I got ahold of. It's been really hard to reach you. I've been trying."
            },
            {
                "speaker": "Bobby",
                "text": "To call you for a."
            },
            {
                "speaker": "Bobby",
                "text": "While who has it? Yeah, it has. But I guess you're really busy, so I'm glad that I got ahold of you and I wanted to talk to you about your treatment and your injury claim."
            },
            {
                "speaker": "Emily",
                "text": "OK. What did you want to talk about specifically? Well."
            },
            {
                "speaker": "Bobby",
                "text": "I want to talk to you about how your treatment is going, So I've noticed that."
            },
            {
                "speaker": "Bobby",
                "text": "Been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist. I see that your doctor had recommended it to before and I want to follow up to see if you've been doing that or if you've talked."
            },
            {
                "speaker": "Emily",
                "text": "To them, yeah, it's been kind of easier just to go to my massage therapist because I can get appointments. I was hoping I could find a physiotherapist in the same clinic, but I couldn't, so I thought it was just easier to keep going to my massage."
            },
            {
                "speaker": "Bobby",
                "text": "Therapist. OK, well, I want you to know that it's been."
            },
            {
                "speaker": "Bobby",
                "text": "About a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time."
            },
            {
                "speaker": "Emily",
                "text": "Oh, OK Well, my massage therapist kept booking me in, so I thought I was just good to keep going."
            },
            {
                "speaker": "Bobby",
                "text": "There. Yeah, I can see that. And we approved the last treatment request that your massage therapy sent in. But to be honest with you, I'm not going to prove the next one. I did talk to you about talking to your physiotherapist and making that call. So you're going to need to do that if you want to keep having treatment."
            },
            {
                "speaker": "Bobby",
                "text": "Provided under your claim."
            },
            {
                "speaker": "Bobby",
                "text": "Well, you mentioned that you're still having problems with your knee and you're fine now. Is that what you're saying?"
            },
            {
                "speaker": "Emily",
                "text": "Yeah, I mean, it still hurts, but I think, you know, it could be worse. So."
            },
            {
                "speaker": "Bobby",
                "text": "Well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards, so."
            },
            {
                "speaker": "Bobby",
                "text": "When we talked and I gave you the information I you are expected to follow it. You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better."
            },
            {
                "speaker": "Emily",
                "text": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too if I don't get any more."
            },
            {
                "speaker": "Bobby",
                "text": "Treatment. Well, I really want you to reach out and call your physiotherapist since you haven't done it yet and this is the third time you've talked about it. If you could please give me a call back next week."
            },
            {
                "speaker": "Bobby",
                "text": "Let's try to do that so that you're talking to them by then and I would like to get an update from you. If I don't, then I don't think I'll be able to approve any more of."
            },
            {
                "speaker": "Emily",
                "text": "The massage either OK, So what happens if I need more treatment, though, or if I feel like I'm still in pain or I'm not able to?"
            },
            {
                "speaker": "Bobby",
                "text": "Do all of my regular stuff well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's going to be really difficult for us to approve any more for you."
            },
            {
                "speaker": "Bobby",
                "text": "Really. I mean, I've talked to you before and I put the notes in your file here that you're not following the advice that."
            },
            {
                "speaker": "Emily",
                "text": "You were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just messed up. Forgot. But yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore."
            },
            {
                "speaker": "Bobby",
                "text": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next. Again, if I don't hear back from by next week, then we won't be approving any more."
            },
            {
                "speaker": "Bobby",
                "text": "Treatment."
            },
            {
                "speaker": "Emily",
                "text": "OK. OK. Well, I'll try to follow up then with the physiotherapist and I'll try to get back to you next week is."
            },
            {
                "speaker": "Bobby",
                "text": "There anything else that I should be doing? No. You have my number and like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of."
            },
            {
                "speaker": "Bobby",
                "text": "You so you know what time I work, so please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today."
            },
            {
                "speaker": "Bobby",
                "text": "OK. Bye."
            }
        ],
        "flags": [
            {
                "speaker": "Bobby",
                "text": "Oh, hi, Emily. I'm glad I got ahold of. It's been really hard to reach you. I've been trying.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.93,
                    "neutral": 0.06
                }
            },
            {
                "speaker": "Bobby",
                "text": "Do all of my regular stuff well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's going to be really difficult for us to approve any more for you.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.87,
                    "neutral": 0.11
                }
            },
            {
                "speaker": "Emily",
                "text": "You were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just messed up. Forgot. But yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.94,
                    "neutral": 0.05
                }
            },
            {
                "speaker": "Bobby",
                "text": "You so you know what time I work, so please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.02,
                    "negative": 0.93,
                    "neutral": 0.05
                }
            }
        ]
    },
    "long": {
        "durationInTicks": 2603600000,
        "conversations": [
          {
            "id": 0,
            "offset": "PT3.6S",
            "offset_in_ticks": 36000000.0,
            "text": "Hi, this is Bobby calling from ICBCS Assembly.",
            "itn": "hi this is bobby calling from ICBCS assembly",
            "lexical": "hi this is bobby calling from I C B C S assembly",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 1,
            "offset": "PT3.6S",
            "offset_in_ticks": 36000000.0,
            "text": "Hi, this is Bobby calling from ICBCS Assembly.",
            "itn": "hi this is bobby calling from ICBCS assembly",
            "lexical": "hi this is bobby calling from I C B C S assembly",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 2,
            "offset": "PT6.76S",
            "offset_in_ticks": 67600000.0,
            "text": "Hi, this is Emily.",
            "itn": "hi this is emily",
            "lexical": "hi this is emily",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 3,
            "offset": "PT6.76S",
            "offset_in_ticks": 67600000.0,
            "text": "Hi, this is Emily.",
            "itn": "hi this is emily",
            "lexical": "hi this is emily",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 4,
            "offset": "PT7.68S",
            "offset_in_ticks": 76800000.0,
            "text": "Yes.",
            "itn": "yes",
            "lexical": "yes",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 5,
            "offset": "PT7.68S",
            "offset_in_ticks": 76800000.0,
            "text": "Yes.",
            "itn": "yes",
            "lexical": "yes",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 6,
            "offset": "PT8.4S",
            "offset_in_ticks": 84000000.0,
            "text": "Oh, hi, Emily.",
            "itn": "oh hi emily",
            "lexical": "oh hi emily",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 7,
            "offset": "PT8.4S",
            "offset_in_ticks": 84000000.0,
            "text": "Oh, hi, Emily.",
            "itn": "oh hi emily",
            "lexical": "oh hi emily",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 8,
            "offset": "PT9.16S",
            "offset_in_ticks": 91600000.0,
            "text": "I'm glad I got a hold of you.",
            "itn": "i'm glad i got a hold of you",
            "lexical": "i'm glad i got a hold of you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 9,
            "offset": "PT9.16S",
            "offset_in_ticks": 91600000.0,
            "text": "I'm glad I got a hold of you.",
            "itn": "i'm glad i got a hold of you",
            "lexical": "i'm glad i got a hold of you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 10,
            "offset": "PT10.56S",
            "offset_in_ticks": 105600000.0,
            "text": "It's been really hard to reach you.",
            "itn": "it's been really hard to reach you",
            "lexical": "it's been really hard to reach you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 11,
            "offset": "PT10.56S",
            "offset_in_ticks": 105600000.0,
            "text": "It's been really hard to reach you.",
            "itn": "it's been really hard to reach you",
            "lexical": "it's been really hard to reach you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 12,
            "offset": "PT11.56S",
            "offset_in_ticks": 115600000.0,
            "text": "I've been trying to call you for a while.",
            "itn": "i've been trying to call you for a while",
            "lexical": "i've been trying to call you for a while",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 13,
            "offset": "PT11.56S",
            "offset_in_ticks": 115600000.0,
            "text": "I've been trying to call you for a while.",
            "itn": "i've been trying to call you for a while",
            "lexical": "i've been trying to call you for a while",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 14,
            "offset": "PT13.48S",
            "offset_in_ticks": 134800000.0,
            "text": "Oh, has it?",
            "itn": "oh has it",
            "lexical": "oh has it",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 15,
            "offset": "PT13.48S",
            "offset_in_ticks": 134800000.0,
            "text": "Oh, has it?",
            "itn": "oh has it",
            "lexical": "oh has it",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 16,
            "offset": "PT14.68S",
            "offset_in_ticks": 146800000.0,
            "text": "Yeah, it has.",
            "itn": "yeah it has",
            "lexical": "yeah it has",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 17,
            "offset": "PT14.68S",
            "offset_in_ticks": 146800000.0,
            "text": "Yeah, it has.",
            "itn": "yeah it has",
            "lexical": "yeah it has",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 18,
            "offset": "PT15.48S",
            "offset_in_ticks": 154800000.0,
            "text": "But I guess you're really busy.",
            "itn": "but i guess you're really busy",
            "lexical": "but i guess you're really busy",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 19,
            "offset": "PT15.48S",
            "offset_in_ticks": 154800000.0,
            "text": "But I guess you're really busy.",
            "itn": "but i guess you're really busy",
            "lexical": "but i guess you're really busy",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 20,
            "offset": "PT17.4S",
            "offset_in_ticks": 174000000.0,
            "text": "So I'm glad that I got a hold of you.",
            "itn": "so i'm glad that i got a hold of you",
            "lexical": "so i'm glad that i got a hold of you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 21,
            "offset": "PT17.4S",
            "offset_in_ticks": 174000000.0,
            "text": "So I'm glad that I got a hold of you.",
            "itn": "so i'm glad that i got a hold of you",
            "lexical": "so i'm glad that i got a hold of you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 22,
            "offset": "PT19.52S",
            "offset_in_ticks": 195200000.0,
            "text": "And I wanted to talk to you about your treatment and your injury claim.",
            "itn": "and i wanted to talk to you about your treatment and your injury claim",
            "lexical": "and i wanted to talk to you about your treatment and your injury claim",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 23,
            "offset": "PT19.52S",
            "offset_in_ticks": 195200000.0,
            "text": "And I wanted to talk to you about your treatment and your injury claim.",
            "itn": "and i wanted to talk to you about your treatment and your injury claim",
            "lexical": "and i wanted to talk to you about your treatment and your injury claim",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 24,
            "offset": "PT24.56S",
            "offset_in_ticks": 245600000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 25,
            "offset": "PT24.56S",
            "offset_in_ticks": 245600000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 26,
            "offset": "PT25.56S",
            "offset_in_ticks": 255600000.0,
            "text": "What did you want to talk about specifically?",
            "itn": "what did you want to talk about specifically",
            "lexical": "what did you want to talk about specifically",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 27,
            "offset": "PT25.56S",
            "offset_in_ticks": 255600000.0,
            "text": "What did you want to talk about specifically?",
            "itn": "what did you want to talk about specifically",
            "lexical": "what did you want to talk about specifically",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 28,
            "offset": "PT28.68S",
            "offset_in_ticks": 286800000.0,
            "text": "Well, I want to talk to you about how your treatment is going.",
            "itn": "well i want to talk to you about how your treatment is going",
            "lexical": "well i want to talk to you about how your treatment is going",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 29,
            "offset": "PT28.68S",
            "offset_in_ticks": 286800000.0,
            "text": "Well, I want to talk to you about how your treatment is going.",
            "itn": "well i want to talk to you about how your treatment is going",
            "lexical": "well i want to talk to you about how your treatment is going",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 30,
            "offset": "PT31.16S",
            "offset_in_ticks": 311600000.0,
            "text": "So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist.",
            "itn": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
            "lexical": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 31,
            "offset": "PT31.16S",
            "offset_in_ticks": 311600000.0,
            "text": "So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist.",
            "itn": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
            "lexical": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 32,
            "offset": "PT42.32S",
            "offset_in_ticks": 423200000.0,
            "text": "I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them.",
            "itn": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
            "lexical": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 33,
            "offset": "PT42.32S",
            "offset_in_ticks": 423200000.0,
            "text": "I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them.",
            "itn": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
            "lexical": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 34,
            "offset": "PT50S",
            "offset_in_ticks": 500000000.0,
            "text": "Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments.",
            "itn": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
            "lexical": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 35,
            "offset": "PT50S",
            "offset_in_ticks": 500000000.0,
            "text": "Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments.",
            "itn": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
            "lexical": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 36,
            "offset": "PT55.56S",
            "offset_in_ticks": 555600000.0,
            "text": "I was hoping I could find a physiotherapist in the same clinic, but I couldn't.",
            "itn": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
            "lexical": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 37,
            "offset": "PT55.56S",
            "offset_in_ticks": 555600000.0,
            "text": "I was hoping I could find a physiotherapist in the same clinic, but I couldn't.",
            "itn": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
            "lexical": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 38,
            "offset": "PT59.4S",
            "offset_in_ticks": 594000000.0,
            "text": "So I thought it was just easier to keep going to my massage therapist.",
            "itn": "so i thought it was just easier to keep going to my massage therapist",
            "lexical": "so i thought it was just easier to keep going to my massage therapist",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 39,
            "offset": "PT59.4S",
            "offset_in_ticks": 594000000.0,
            "text": "So I thought it was just easier to keep going to my massage therapist.",
            "itn": "so i thought it was just easier to keep going to my massage therapist",
            "lexical": "so i thought it was just easier to keep going to my massage therapist",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 40,
            "offset": "PT1M3.16S",
            "offset_in_ticks": 631600000.0,
            "text": "OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time.",
            "itn": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
            "lexical": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 41,
            "offset": "PT1M3.16S",
            "offset_in_ticks": 631600000.0,
            "text": "OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time.",
            "itn": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
            "lexical": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 42,
            "offset": "PT1M15.96S",
            "offset_in_ticks": 759600000.0,
            "text": "Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there.",
            "itn": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
            "lexical": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 43,
            "offset": "PT1M15.96S",
            "offset_in_ticks": 759600000.0,
            "text": "Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there.",
            "itn": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
            "lexical": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 44,
            "offset": "PT1M22.24S",
            "offset_in_ticks": 822400000.0,
            "text": "Yeah, I can see that.",
            "itn": "yeah i can see that",
            "lexical": "yeah i can see that",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 45,
            "offset": "PT1M22.24S",
            "offset_in_ticks": 822400000.0,
            "text": "Yeah, I can see that.",
            "itn": "yeah i can see that",
            "lexical": "yeah i can see that",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 46,
            "offset": "PT1M23.28S",
            "offset_in_ticks": 832800000.0,
            "text": "And we approved the last treatment request that your massage therapist sent in.",
            "itn": "and we approved the last treatment request that your massage therapist sent in",
            "lexical": "and we approved the last treatment request that your massage therapist sent in",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 47,
            "offset": "PT1M23.28S",
            "offset_in_ticks": 832800000.0,
            "text": "And we approved the last treatment request that your massage therapist sent in.",
            "itn": "and we approved the last treatment request that your massage therapist sent in",
            "lexical": "and we approved the last treatment request that your massage therapist sent in",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 48,
            "offset": "PT1M28.36S",
            "offset_in_ticks": 883600000.0,
            "text": "But to be honest with you, I'm not going to prove the next one.",
            "itn": "but to be honest with you i'm not going to prove the next one",
            "lexical": "but to be honest with you i'm not going to prove the next one",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 49,
            "offset": "PT1M28.36S",
            "offset_in_ticks": 883600000.0,
            "text": "But to be honest with you, I'm not going to prove the next one.",
            "itn": "but to be honest with you i'm not going to prove the next one",
            "lexical": "but to be honest with you i'm not going to prove the next one",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 50,
            "offset": "PT1M30.88S",
            "offset_in_ticks": 908800000.0,
            "text": "I did talk to you about talking to your physiotherapist and making that call.",
            "itn": "i did talk to you about talking to your physiotherapist and making that call",
            "lexical": "i did talk to you about talking to your physiotherapist and making that call",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 51,
            "offset": "PT1M30.88S",
            "offset_in_ticks": 908800000.0,
            "text": "I did talk to you about talking to your physiotherapist and making that call.",
            "itn": "i did talk to you about talking to your physiotherapist and making that call",
            "lexical": "i did talk to you about talking to your physiotherapist and making that call",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 52,
            "offset": "PT1M34.28S",
            "offset_in_ticks": 942800000.0,
            "text": "So you're going to need to do that if you want to keep having treatment provided under your claim.",
            "itn": "so you're going to need to do that if you want to keep having treatment provided under your claim",
            "lexical": "so you're going to need to do that if you want to keep having treatment provided under your claim",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 53,
            "offset": "PT1M34.28S",
            "offset_in_ticks": 942800000.0,
            "text": "So you're going to need to do that if you want to keep having treatment provided under your claim.",
            "itn": "so you're going to need to do that if you want to keep having treatment provided under your claim",
            "lexical": "so you're going to need to do that if you want to keep having treatment provided under your claim",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 54,
            "offset": "PT1M39.36S",
            "offset_in_ticks": 993600000.0,
            "text": "OK, that makes sense.",
            "itn": "OK that makes sense",
            "lexical": "OK that makes sense",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 55,
            "offset": "PT1M39.36S",
            "offset_in_ticks": 993600000.0,
            "text": "OK, that makes sense.",
            "itn": "OK that makes sense",
            "lexical": "OK that makes sense",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 56,
            "offset": "PT1M40.76S",
            "offset_in_ticks": 1007600000.0,
            "text": "I can do that.",
            "itn": "i can do that",
            "lexical": "i can do that",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 57,
            "offset": "PT1M40.76S",
            "offset_in_ticks": 1007600000.0,
            "text": "I can do that.",
            "itn": "i can do that",
            "lexical": "i can do that",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 58,
            "offset": "PT1M41.36S",
            "offset_in_ticks": 1013600000.0,
            "text": "You know what?",
            "itn": "you know what",
            "lexical": "you know what",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 59,
            "offset": "PT1M41.36S",
            "offset_in_ticks": 1013600000.0,
            "text": "You know what?",
            "itn": "you know what",
            "lexical": "you know what",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 60,
            "offset": "PT1M41.76S",
            "offset_in_ticks": 1017600000.0,
            "text": "I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment.",
            "itn": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
            "lexical": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 61,
            "offset": "PT1M41.76S",
            "offset_in_ticks": 1017600000.0,
            "text": "I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment.",
            "itn": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
            "lexical": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 62,
            "offset": "PT1M49.48S",
            "offset_in_ticks": 1094800000.0,
            "text": "Well, you mentioned that you're still having problems with your knee and you're fine now.",
            "itn": "well you mentioned that you're still having problems with your knee and you're fine now",
            "lexical": "well you mentioned that you're still having problems with your knee and you're fine now",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 63,
            "offset": "PT1M49.48S",
            "offset_in_ticks": 1094800000.0,
            "text": "Well, you mentioned that you're still having problems with your knee and you're fine now.",
            "itn": "well you mentioned that you're still having problems with your knee and you're fine now",
            "lexical": "well you mentioned that you're still having problems with your knee and you're fine now",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 64,
            "offset": "PT1M54.92S",
            "offset_in_ticks": 1149200000.0,
            "text": "Is that what you're saying?",
            "itn": "is that what you're saying",
            "lexical": "is that what you're saying",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 65,
            "offset": "PT1M54.92S",
            "offset_in_ticks": 1149200000.0,
            "text": "Is that what you're saying?",
            "itn": "is that what you're saying",
            "lexical": "is that what you're saying",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 66,
            "offset": "PT1M56.36S",
            "offset_in_ticks": 1163600000.0,
            "text": "Yeah.",
            "itn": "yeah",
            "lexical": "yeah",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 67,
            "offset": "PT1M56.36S",
            "offset_in_ticks": 1163600000.0,
            "text": "Yeah.",
            "itn": "yeah",
            "lexical": "yeah",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 68,
            "offset": "PT1M56.64S",
            "offset_in_ticks": 1166400000.0,
            "text": "I mean, it still hurts, but I think, you know, it could be worse.",
            "itn": "i mean it still hurts but i think you know it could be worse",
            "lexical": "i mean it still hurts but i think you know it could be worse",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 69,
            "offset": "PT1M56.64S",
            "offset_in_ticks": 1166400000.0,
            "text": "I mean, it still hurts, but I think, you know, it could be worse.",
            "itn": "i mean it still hurts but i think you know it could be worse",
            "lexical": "i mean it still hurts but i think you know it could be worse",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 70,
            "offset": "PT2M0.76S",
            "offset_in_ticks": 1207600000.0,
            "text": "So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards.",
            "itn": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
            "lexical": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 71,
            "offset": "PT2M0.76S",
            "offset_in_ticks": 1207600000.0,
            "text": "So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards.",
            "itn": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
            "lexical": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 72,
            "offset": "PT2M9.96S",
            "offset_in_ticks": 1299600000.0,
            "text": "So when we talked and I gave you the information, I you are expected to follow it.",
            "itn": "so when we talked and i gave you the information i you are expected to follow it",
            "lexical": "so when we talked and i gave you the information i you are expected to follow it",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 73,
            "offset": "PT2M9.96S",
            "offset_in_ticks": 1299600000.0,
            "text": "So when we talked and I gave you the information, I you are expected to follow it.",
            "itn": "so when we talked and i gave you the information i you are expected to follow it",
            "lexical": "so when we talked and i gave you the information i you are expected to follow it",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 74,
            "offset": "PT2M15.24S",
            "offset_in_ticks": 1352400000.0,
            "text": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better.",
            "itn": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
            "lexical": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 75,
            "offset": "PT2M15.24S",
            "offset_in_ticks": 1352400000.0,
            "text": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better.",
            "itn": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
            "lexical": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 76,
            "offset": "PT2M23.72S",
            "offset_in_ticks": 1437200000.0,
            "text": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too.",
            "itn": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
            "lexical": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 77,
            "offset": "PT2M23.72S",
            "offset_in_ticks": 1437200000.0,
            "text": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too.",
            "itn": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
            "lexical": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 78,
            "offset": "PT2M32.4S",
            "offset_in_ticks": 1524000000.0,
            "text": "If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist.",
            "itn": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
            "lexical": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 79,
            "offset": "PT2M32.4S",
            "offset_in_ticks": 1524000000.0,
            "text": "If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist.",
            "itn": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
            "lexical": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 80,
            "offset": "PT2M37.76S",
            "offset_in_ticks": 1577600000.0,
            "text": "And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week.",
            "itn": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
            "lexical": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 81,
            "offset": "PT2M37.76S",
            "offset_in_ticks": 1577600000.0,
            "text": "And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week.",
            "itn": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
            "lexical": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 82,
            "offset": "PT2M43.68S",
            "offset_in_ticks": 1636800000.0,
            "text": "Let's try to do that so that you're talking to them by then.",
            "itn": "let's try to do that so that you're talking to them by then",
            "lexical": "let's try to do that so that you're talking to them by then",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 83,
            "offset": "PT2M43.68S",
            "offset_in_ticks": 1636800000.0,
            "text": "Let's try to do that so that you're talking to them by then.",
            "itn": "let's try to do that so that you're talking to them by then",
            "lexical": "let's try to do that so that you're talking to them by then",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 84,
            "offset": "PT2M46.08S",
            "offset_in_ticks": 1660800000.0,
            "text": "And I would like to get an update from you.",
            "itn": "and i would like to get an update from you",
            "lexical": "and i would like to get an update from you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 85,
            "offset": "PT2M46.08S",
            "offset_in_ticks": 1660800000.0,
            "text": "And I would like to get an update from you.",
            "itn": "and i would like to get an update from you",
            "lexical": "and i would like to get an update from you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 86,
            "offset": "PT2M47.88S",
            "offset_in_ticks": 1678800000.0,
            "text": "If I don't, then I don't think I'll be able to approve any more of the massage either.",
            "itn": "if i don't then i don't think i'll be able to approve any more of the massage either",
            "lexical": "if i don't then i don't think i'll be able to approve any more of the massage either",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 87,
            "offset": "PT2M47.88S",
            "offset_in_ticks": 1678800000.0,
            "text": "If I don't, then I don't think I'll be able to approve any more of the massage either.",
            "itn": "if i don't then i don't think i'll be able to approve any more of the massage either",
            "lexical": "if i don't then i don't think i'll be able to approve any more of the massage either",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 88,
            "offset": "PT2M53.44S",
            "offset_in_ticks": 1734400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 89,
            "offset": "PT2M53.44S",
            "offset_in_ticks": 1734400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 90,
            "offset": "PT2M53.88S",
            "offset_in_ticks": 1738800000.0,
            "text": "So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff?",
            "itn": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
            "lexical": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 91,
            "offset": "PT2M53.88S",
            "offset_in_ticks": 1738800000.0,
            "text": "So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff?",
            "itn": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
            "lexical": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 92,
            "offset": "PT3M2.2S",
            "offset_in_ticks": 1822000000.0,
            "text": "Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back.",
            "itn": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
            "lexical": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 93,
            "offset": "PT3M2.2S",
            "offset_in_ticks": 1822000000.0,
            "text": "Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back.",
            "itn": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
            "lexical": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 94,
            "offset": "PT3M9.36S",
            "offset_in_ticks": 1893600000.0,
            "text": "But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you.",
            "itn": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
            "lexical": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 95,
            "offset": "PT3M9.36S",
            "offset_in_ticks": 1893600000.0,
            "text": "But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you.",
            "itn": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
            "lexical": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 96,
            "offset": "PT3M16.16S",
            "offset_in_ticks": 1961600000.0,
            "text": "Really.",
            "itn": "really",
            "lexical": "really",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 97,
            "offset": "PT3M16.16S",
            "offset_in_ticks": 1961600000.0,
            "text": "Really.",
            "itn": "really",
            "lexical": "really",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 98,
            "offset": "PT3M16.52S",
            "offset_in_ticks": 1965200000.0,
            "text": "I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given.",
            "itn": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
            "lexical": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 99,
            "offset": "PT3M16.52S",
            "offset_in_ticks": 1965200000.0,
            "text": "I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given.",
            "itn": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
            "lexical": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 100,
            "offset": "PT3M23.04S",
            "offset_in_ticks": 2030400000.0,
            "text": "Oh, OK.",
            "itn": "oh OK",
            "lexical": "oh OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 101,
            "offset": "PT3M23.04S",
            "offset_in_ticks": 2030400000.0,
            "text": "Oh, OK.",
            "itn": "oh OK",
            "lexical": "oh OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 102,
            "offset": "PT3M24S",
            "offset_in_ticks": 2040000000.0,
            "text": "Well, I'm really sorry.",
            "itn": "well i'm really sorry",
            "lexical": "well i'm really sorry",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 103,
            "offset": "PT3M24S",
            "offset_in_ticks": 2040000000.0,
            "text": "Well, I'm really sorry.",
            "itn": "well i'm really sorry",
            "lexical": "well i'm really sorry",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 104,
            "offset": "PT3M25.44S",
            "offset_in_ticks": 2054400000.0,
            "text": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me.",
            "itn": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
            "lexical": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 105,
            "offset": "PT3M25.44S",
            "offset_in_ticks": 2054400000.0,
            "text": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me.",
            "itn": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
            "lexical": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 106,
            "offset": "PT3M31.16S",
            "offset_in_ticks": 2111600000.0,
            "text": "I just must have forgot, but yeah, OK, I can do what you told me and I'll.",
            "itn": "i just must have forgot but yeah OK i can do what you told me and i'll",
            "lexical": "i just must have forgot but yeah OK i can do what you told me and i'll",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 107,
            "offset": "PT3M31.16S",
            "offset_in_ticks": 2111600000.0,
            "text": "I just must have forgot, but yeah, OK, I can do what you told me and I'll.",
            "itn": "i just must have forgot but yeah OK i can do what you told me and i'll",
            "lexical": "i just must have forgot but yeah OK i can do what you told me and i'll",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 108,
            "offset": "PT3M36.12S",
            "offset_in_ticks": 2161200000.0,
            "text": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there.",
            "itn": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
            "lexical": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 109,
            "offset": "PT3M36.12S",
            "offset_in_ticks": 2161200000.0,
            "text": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there.",
            "itn": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
            "lexical": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 110,
            "offset": "PT3M40.24S",
            "offset_in_ticks": 2202400000.0,
            "text": "But if not, I guess I just won't bother you anymore.",
            "itn": "but if not i guess i just won't bother you anymore",
            "lexical": "but if not i guess i just won't bother you anymore",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 111,
            "offset": "PT3M40.24S",
            "offset_in_ticks": 2202400000.0,
            "text": "But if not, I guess I just won't bother you anymore.",
            "itn": "but if not i guess i just won't bother you anymore",
            "lexical": "but if not i guess i just won't bother you anymore",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 112,
            "offset": "PT3M45.28S",
            "offset_in_ticks": 2252800000.0,
            "text": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next.",
            "itn": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
            "lexical": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 113,
            "offset": "PT3M45.28S",
            "offset_in_ticks": 2252800000.0,
            "text": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next.",
            "itn": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
            "lexical": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 114,
            "offset": "PT3M49.88S",
            "offset_in_ticks": 2298800000.0,
            "text": "Again, if I don't hear back from by next week, then we won't be approving any more treatment.",
            "itn": "again if i don't hear back from by next week then we won't be approving any more treatment",
            "lexical": "again if i don't hear back from by next week then we won't be approving any more treatment",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 115,
            "offset": "PT3M49.88S",
            "offset_in_ticks": 2298800000.0,
            "text": "Again, if I don't hear back from by next week, then we won't be approving any more treatment.",
            "itn": "again if i don't hear back from by next week then we won't be approving any more treatment",
            "lexical": "again if i don't hear back from by next week then we won't be approving any more treatment",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 116,
            "offset": "PT3M55.64S",
            "offset_in_ticks": 2356400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 117,
            "offset": "PT3M55.64S",
            "offset_in_ticks": 2356400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 118,
            "offset": "PT3M56.24S",
            "offset_in_ticks": 2362400000.0,
            "text": "OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week.",
            "itn": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
            "lexical": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 119,
            "offset": "PT3M56.24S",
            "offset_in_ticks": 2362400000.0,
            "text": "OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week.",
            "itn": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
            "lexical": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 120,
            "offset": "PT4M0.32S",
            "offset_in_ticks": 2403200000.0,
            "text": "Is there anything else that I should be doing?",
            "itn": "is there anything else that i should be doing",
            "lexical": "is there anything else that i should be doing",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 121,
            "offset": "PT4M0.32S",
            "offset_in_ticks": 2403200000.0,
            "text": "Is there anything else that I should be doing?",
            "itn": "is there anything else that i should be doing",
            "lexical": "is there anything else that i should be doing",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 122,
            "offset": "PT4M2.28S",
            "offset_in_ticks": 2422800000.0,
            "text": "No.",
            "itn": "no",
            "lexical": "no",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 123,
            "offset": "PT4M2.28S",
            "offset_in_ticks": 2422800000.0,
            "text": "No.",
            "itn": "no",
            "lexical": "no",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 124,
            "offset": "PT4M2.48S",
            "offset_in_ticks": 2424800000.0,
            "text": "You have my number.",
            "itn": "you have my number",
            "lexical": "you have my number",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 125,
            "offset": "PT4M2.48S",
            "offset_in_ticks": 2424800000.0,
            "text": "You have my number.",
            "itn": "you have my number",
            "lexical": "you have my number",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 126,
            "offset": "PT4M3.16S",
            "offset_in_ticks": 2431600000.0,
            "text": "And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you.",
            "itn": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
            "lexical": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 127,
            "offset": "PT4M3.16S",
            "offset_in_ticks": 2431600000.0,
            "text": "And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you.",
            "itn": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
            "lexical": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 128,
            "offset": "PT4M7.64S",
            "offset_in_ticks": 2476400000.0,
            "text": "So you know what time I work.",
            "itn": "so you know what time i work",
            "lexical": "so you know what time i work",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 129,
            "offset": "PT4M7.64S",
            "offset_in_ticks": 2476400000.0,
            "text": "So you know what time I work.",
            "itn": "so you know what time i work",
            "lexical": "so you know what time i work",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 130,
            "offset": "PT4M9.6S",
            "offset_in_ticks": 2496000000.0,
            "text": "So please give me a call.",
            "itn": "so please give me a call",
            "lexical": "so please give me a call",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 131,
            "offset": "PT4M9.6S",
            "offset_in_ticks": 2496000000.0,
            "text": "So please give me a call.",
            "itn": "so please give me a call",
            "lexical": "so please give me a call",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 132,
            "offset": "PT4M10.64S",
            "offset_in_ticks": 2506400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 133,
            "offset": "PT4M10.64S",
            "offset_in_ticks": 2506400000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 134,
            "offset": "PT4M11.04S",
            "offset_in_ticks": 2510400000.0,
            "text": "I'm really sorry about that.",
            "itn": "i'm really sorry about that",
            "lexical": "i'm really sorry about that",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 135,
            "offset": "PT4M11.04S",
            "offset_in_ticks": 2510400000.0,
            "text": "I'm really sorry about that.",
            "itn": "i'm really sorry about that",
            "lexical": "i'm really sorry about that",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 136,
            "offset": "PT4M12.4S",
            "offset_in_ticks": 2524000000.0,
            "text": "Thanks so much for calling me today.",
            "itn": "thanks so much for calling me today",
            "lexical": "thanks so much for calling me today",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 137,
            "offset": "PT4M12.4S",
            "offset_in_ticks": 2524000000.0,
            "text": "Thanks so much for calling me today.",
            "itn": "thanks so much for calling me today",
            "lexical": "thanks so much for calling me today",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 138,
            "offset": "PT4M14S",
            "offset_in_ticks": 2540000000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 139,
            "offset": "PT4M14S",
            "offset_in_ticks": 2540000000.0,
            "text": "OK.",
            "itn": "OK",
            "lexical": "OK",
            "role": "Customer",
            "participantId": 1
          },
          {
            "id": 140,
            "offset": "PT4M14.48S",
            "offset_in_ticks": 2544800000.0,
            "text": "Bye.",
            "itn": "bye",
            "lexical": "bye",
            "role": "Agent",
            "participantId": 0
          },
          {
            "id": 141,
            "offset": "PT4M14.48S",
            "offset_in_ticks": 2544800000.0,
            "text": "Bye.",
            "itn": "bye",
            "lexical": "bye",
            "role": "Customer",
            "participantId": 1
          }
        ]
      }
}
        ]
    }

    # response = {
    #     "calls": [
    #         {
    #             "representativeName": "Adrian Smith",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Bobby",
    #     "summary": "Call the customer to check status of treatment plan",
    #     "callLength": 15,
    #     "date": "04/21/2024",
    #     "flags": [
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 2
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": True,
    #                 "timestamp": 4
    #             },
    #             {
    #                 "isCustomer": False,
    #                 "isRepresentative": True,
    #                 "timestamp": 10
    #             }
    #         ]
    #         },
    #         {
    #             "representativeName": "Emma Park",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Jane Doe",
    #     "summary": "Call the customer to check about expenses",
    #     "callLength": 20,
    #     "date": "04/23/2024",
    #     "flags": [
    #         ]
    #         },
    #         {
    #             "representativeName": "Eddie Edwards",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Alex Black",
    #     "summary": "Call about claimstatus",
    #     "callLength": 27,
    #     "date": "04/12/2024",
    #     "flags": [
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 2
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 4
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 10
    #             }
    #         ]
    #         }
    #     ]
        
    # }

    return func.HttpResponse(json.dumps(response, default=str),
                status_code=200                
            )
    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )