#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bot.py

import os
import re
import socket
import random
import requests
import datetime
import math
import csv
from names import *
from config import *
from time import sleep
from decimal import *

s = socket.socket()
s.connect((Host, Port))
s.send("PASS {}\r\n".format("oauth:" + Token).encode("utf-8"))
s.send("NICK {}\r\n".format(Nickname).encode("utf-8"))
s.send("JOIN {}\r\n".format(Channel).encode("utf-8"))

def randomEmote():
    emotes = ["Kappa", "MrDestructoid", "BCWarrior", "DansGame", "SwiftRage", "PJSalt", "Kreygasm", "SSSsss", "PunchTrees", "FunRun", "SMOrc", "FrankerZ", "BibleThump", "PogChamp", "ResidentSleeper", "4Head", "FailFish", "Keepo", "ANELE", "BrokeBack", "EleGiggle", "BabyRage", "panicBasket", "WutFace", "HeyGuys", "KappaPride", "CoolCat", "NotLikeThis", "riPepperonis", "duDudu", "bleedPurple", "SeemsGood", "MingLee", "KappaRoss", "KappaClaus", "OhMyDog", "OPFrog", "SeriousSloth", "KomodoHype", "VoHiYo", "KappaWealth", "cmonBruh", "NomNom", "StinkyCheese", "ChefFrank", "FutureMan", "OpieOP", "DxCat", "GivePLZ", "TakeNRG", "Jebaited", "CurseLit", "TriHard", "CoolStoryBob", "ItsBoshyTime", "PartyTime", "TheIlluminati", "BlessRNG", "TwitchLit", "CarlSmile", "Squid3", "VaultBoy", "LUL", "PowerUpR", "PowerUpL"]
    randomNumber = random.randint(0, len(emotes))
    randomEmote = emotes[randomNumber]
    return randomEmote

def sender():
    m = re.search(':(.+?)!', data)
    sender= m.group(1)
    return sender

def add():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    addingNumbers = sum(makingNumbers)
    everythingTogether = ' + '.join(map(str, makingNumbers)) + ' = ' + str(addingNumbers)
    return everythingTogether

def multiply():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    total = 1
    for x in makingNumbers:
        total *= x
    everythingTogether = ' * '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether

def divide():
    test = data.split()[4:]
    makingNumbers = [int(i) for i in test]
    total = makingNumbers[0]
    for x in makingNumbers[1:]:
        total /= x
    everythingTogether = ' / '.join(map(str, makingNumbers)) + ' = ' + str(total)
    return everythingTogether

def lick():
    over = " over and "
    randomNumber = random.randint(1, 30)
    licks = over * randomNumber + "over again (x" + str(randomNumber) + ")"
    return licks

def subscribers():
    # url = "https://api.twitch.tv/kraken/channels/" + User_ID_ridgure
    # params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token, "Accept": "application/vnd.twitchtv.v5+json"}
    # response = requests.get(url, headers=params).json()

    # responds
    # {u'private_video': False,
    # u'updated_at': u'2018-11-26T00:23:37Z',
    # u'privacy_options_enabled': False,
    # u'video_banner': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ridgure-channel_offline_image-3c60c59d9ba5c169-1920x1080.png',
    # u'partner': False,
    # u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ee5101dc-3ddb-43aa-a887-a569414a8844-profile_image-300x300.png',
    # u'display_name': u'Ridgure',
    # u'followers': 720,
    # u'broadcaster_software': u'unknown_rtmp',
    # u'broadcaster_language': u'en',
    # u'broadcaster_type': u'affiliate',
    # u'status': u'Making the Asakusa Tourism Center by Kengo Kuma | Architecture',
    # u'description': u'I stream every Wednesday from 7-12 CET. You can expect entertainment and other fun as well as an awesome community of chatters and other streamers that hang out when I am live.',
    # u'views': 11096,
    # u'game': u'Art',
    # u'name': u'ridgure',
    # u'language': u'en',
    # u'url': u'https://www.twitch.tv/ridgure',
    # u'created_at': u'2015-11-08T22:14:42Z',
    # u'mature': True,
    # u'profile_banner_background_color': u'#000000',
    # u'_id': u'106586349',
    # u'profile_banner': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ridgure-profile_banner-aab842adb656bc98-480.png'}

    # Use this url for getting the token
    # url = "https://id.twitch.tv/oauth2/authorize?client_id=" + ClientID + "&redirect_uri=http://localhost&response_type=token&scope=channel_subscriptions+user_read+channel_check_subscription+chat_edit+channel_moderate+chat_login"

    url = "https://api.twitch.tv/kraken/channels/106586349/subscriptions"
    params = {"Accept": "application/vnd.twitchtv.v5+json", "Client-ID": ClientID, "Authorization": "OAuth " + Token, "limit": "100"}
    response = requests.get(url, headers=params, allow_redirects=True)
    if response.status_code == 429:
        print "Too many subscriber requests"
    global subscriberResponse
    subscriberResponse = response.json()
    return subscriberResponse

    # returns
    # {u'_total': 3,
    # u'subscriptions': [
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure)', u'sub_plan': u'1000',
    #      u'created_at': u'2017-06-28T19:23:44Z', u'user': {
    #         u'bio': u'Just a start up streamer who does a bit of youtube while still working and going to college',
    #         u'display_name': u'LilGamerHelle', u'name': u'lilgamerhelle', u'created_at': u'2012-08-03T19:04:34Z',
    #         u'updated_at': u'2018-11-25T20:13:23Z',
    #         u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/lilgamerhelle-profile_image-bde580adc7af34ad-300x300.png',
    #         u'_id': u'32670426', u'type': u'user'}, u'_id': u'c56ff1e6b85b0bcbbfbbb471b7fe903798ecb9dc'},
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure): $24.99 Sub',
    #      u'sub_plan': u'3000', u'created_at': u'2017-06-28T20:11:45Z', u'user': {
    #         u'bio': u'I stream every Wednesday from 7-12 CET. You can expect entertainment and other fun as well as an awesome community of chatters and other streamers that hang out when I am live.',
    #         u'display_name': u'Ridgure', u'name': u'ridgure', u'created_at': u'2015-11-08T22:14:42Z',
    #         u'updated_at': u'2018-11-27T23:23:47Z',
    #         u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/ee5101dc-3ddb-43aa-a887-a569414a8844-profile_image-300x300.png',
    #         u'_id': u'106586349', u'type': u'user'}, u'_id': u'f6fdc613e0ee25ef84b5d0c16605c4444e9d7b50'},
    #     {u'is_gift': False, u'sender': None, u'sub_plan_name': u'Channel Subscription (ridgure)', u'sub_plan': u'1000',
    #      u'created_at': u'2018-01-03T23:11:27Z',
    #      u'user': {u'bio': u'Rocket League/Minecraft', u'display_name': u'Cirekon', u'name': u'cirekon',
    #                u'created_at': u'2012-07-04T16:10:34Z', u'updated_at': u'2018-11-25T13:14:25Z',
    #                u'logo': u'https://static-cdn.jtvnw.net/jtv_user_pictures/bca68a9164bd54a1-profile_image-300x300.jpeg',
    #                u'_id': u'31861174', u'type': u'user'}, u'_id': u'e7879cef043c356c6b99901f3c89d2e32f1d0543'}
    #  ]}


def followers():
    try:
        url100 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100"
        params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token}
        response = requests.get(url100, headers=params)
        responseFirst100 = response.json()
        if response.status_code == 429:
            print "Too many follower requests"

        global pagination
        pagination = responseFirst100['pagination']['cursor']
        totalFollowers = responseFirst100['total']
        global followerList
        followerList = responseFirst100['data']

        # making a list of all the followers
        for i in xrange(int(math.ceil(totalFollowers / float(100))) - 1):
            url200 = "https://api.twitch.tv/helix/users/follows?to_id=" + User_ID_ridgure + "&first=100&after=" + pagination
            response = requests.get(url200, headers=params).json()
            pagination = response['pagination']['cursor']
            followerList = followerList + response['data']

        return followerList
    except Exception, e:
        pass

    # print response
    # returns
    #{u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjoiMTUxNDI1NDE4NzA4NTAyMDAwMCJ9'},
        # u'total': 421,
    # u'data': [
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T20:11:57Z', u'from_id': u'163393705'},
        # {u'to_id': u'106586349', u'followed_at': u'2018-01-18T06:41:48Z', u'from_id': u'46728242'},

def followAgeAll():
    global followAgeList
    followAgeList = [[] for i in range(len(followerList))]

    for i in xrange(len(followerList)):

        # Get follow Day Month Year
        m = re.search('(.+?)T', followerList[i]['followed_at'])
        followDate = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?)-', followDate)
        followYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', followDate)
        followMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', followDate)
        followDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', followDay)
        followDay = m.group(1).encode('ascii', 'ignore')

        # Get follow Hour Minute Second
        m = re.search('T(.+?)Z', followerList[i]['followed_at'])
        followTime = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?):', followTime)
        followHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', followTime)
        followMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', followTime)
        followSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', followSecond)
        followSecond = m.group(1).encode('ascii', 'ignore')

        # Get current Day Month Year
        currentDate = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        m = re.search('(.+?)-', currentDate)
        currentYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', currentDate)
        currentMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDate)
        currentDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDay)
        currentDay = m.group(1).encode('ascii', 'ignore')

        # Get current Hour Minute Second
        currentTime = datetime.datetime.utcnow().strftime("%H:%M:%S")
        m = re.search('(.+?):', currentTime)
        currentHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', currentTime)
        currentMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentTime)
        currentSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentSecond)
        currentSecond = m.group(1).encode('ascii', 'ignore')

        # Compare follow with current
        followDate = datetime.date(int(followYear), int(followMonth), int(followDay))
        followDateTime = datetime.datetime.combine(followDate, datetime.time(int(followHour), int(followMinute), int(followSecond), 0,  tzinfo=None))
        currentDate = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
        currentDateTime = datetime.datetime.combine(currentDate, datetime.time(int(currentHour), int(currentMinute), int(currentDay), 0,  tzinfo=None))
        deltaDate = currentDateTime - followDateTime
        deltaHours = int(math.floor(deltaDate.seconds / 3600))
        deltaMinutes = int(math.floor((deltaDate.seconds - (deltaHours * 3600)) / 60))
        deltaSeconds = int(deltaDate.seconds - (deltaHours * 3600) - (deltaMinutes * 60))

        # Return array
        followAgeList[i].insert(0, str(deltaDate))
        followAgeList[i].insert(1, deltaDate.days)
        followAgeList[i].insert(2, deltaHours)
        followAgeList[i].insert(3, deltaMinutes)
        followAgeList[i].insert(4, deltaSeconds)
        followAgeList[i].insert(5, deltaDate.seconds)
        followAgeList[i].insert(6, followDateTime)

    return followAgeList


def months_between(date1,date2):
    if date1 > date2:
        date1, date2 = date2, date1
    m1 = date1.year*12+date1.month
    m2 = date2.year*12+date2.month
    months = m2-m1
    if date1.day > date2.day:
        months -= 1
    elif date1.day == date2.day:
        seconds1 = date1.hour*3600+date1.minute+date1.second
        seconds2 = date2.hour*3600+date2.minute+date2.second
        if seconds1 > seconds2:
            months -= 1
    return months

# date1 = dt.datetime.strptime('2011-08-15 12:00:00', '%Y-%m-%d %H:%M:%S')
# date2 = dt.datetime.strptime('2012-02-15', '%Y-%m-%d')
# print(months_between(date1,date2))

def subscribeAgeAll():
    global subscribeAgeList
    subscribeAgeList = [[] for i in range(len(subscriberResponse['subscriptions']))]

    for i in xrange(len(subscriberResponse['subscriptions'])):

        # Get subscribe Day Month Year
        m = re.search('(.+?)T', subscriberResponse['subscriptions'][i]['created_at'])
        subscribeDate = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?)-', subscribeDate)
        subscribeYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', subscribeDate)
        subscribeMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', subscribeDate)
        subscribeDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', subscribeDay)
        subscribeDay = m.group(1).encode('ascii', 'ignore')

        # Get subscribe Hour Minute Second
        m = re.search('T(.+?)Z', subscriberResponse['subscriptions'][i]['created_at'])
        subscribeTime = m.group(1).encode('ascii', 'ignore')
        m = re.search('(.+?):', subscribeTime)
        subscribeHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', subscribeTime)
        subscribeMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', subscribeTime)
        subscribeSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', subscribeSecond)
        subscribeSecond = m.group(1).encode('ascii', 'ignore')

        # Get current Day Month Year
        currentDate = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        m = re.search('(.+?)-', currentDate)
        currentYear = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.+?)-', currentDate)
        currentMonth = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDate)
        currentDay = m.group(1).encode('ascii', 'ignore')
        m = re.search('-(.*)', currentDay)
        currentDay = m.group(1).encode('ascii', 'ignore')

        # Get current Hour Minute Second
        currentTime = datetime.datetime.utcnow().strftime("%H:%M:%S")
        m = re.search('(.+?):', currentTime)
        currentHour = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.+?):', currentTime)
        currentMinute = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentTime)
        currentSecond = m.group(1).encode('ascii', 'ignore')
        m = re.search(':(.*)', currentSecond)
        currentSecond = m.group(1).encode('ascii', 'ignore')

        # Compare subscribe with current
        subscribeDate = datetime.date(int(subscribeYear), int(subscribeMonth), int(subscribeDay))
        subscribeDateTime = datetime.datetime.combine(subscribeDate, datetime.time(int(subscribeHour), int(subscribeMinute), int(subscribeSecond), 0,  tzinfo=None))
        currentDate = datetime.date(int(currentYear), int(currentMonth), int(currentDay))
        currentDateTime = datetime.datetime.combine(currentDate, datetime.time(int(currentHour), int(currentMinute), int(currentDay), 0,  tzinfo=None))
        deltaDate = currentDateTime - subscribeDateTime
        deltaHours = int(math.floor(deltaDate.seconds / 3600))
        deltaMinutes = int(math.floor((deltaDate.seconds - (deltaHours * 3600)) / 60))
        deltaSeconds = int(deltaDate.seconds - (deltaHours * 3600) - (deltaMinutes * 60))

        # Return array
        subscribeAgeList[i].insert(0, str(deltaDate))
        subscribeAgeList[i].insert(1, deltaDate.days)
        subscribeAgeList[i].insert(2, deltaHours)
        subscribeAgeList[i].insert(3, deltaMinutes)
        subscribeAgeList[i].insert(4, deltaSeconds)
        subscribeAgeList[i].insert(5, deltaDate.seconds)
        subscribeAgeList[i].insert(6, subscribeDateTime)

        date1 = datetime.datetime.strptime(str(subscribeYear) + "-" + str(subscribeMonth) + "-" + str(subscribeDay) + " " + str(subscribeHour) + ":" + str(subscribeMinute) + ":" + str(subscribeSecond), '%Y-%m-%d %H:%M:%S')
        date2 = datetime.datetime.strptime(str(currentYear) + "-" + str(currentMonth) + "-" + str(currentDay) + " " + str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond), '%Y-%m-%d %H:%M:%S')
        subscribeAgeList[i].append(months_between(date1, date2))
        subscribeAgeList[i].append(subscriberResponse['subscriptions'][i]['user']['display_name'])
    return subscribeAgeList


def uptime():
    url = "https://api.twitch.tv/helix/streams?user_id=" + User_ID_ridgure
    params = {"Client-ID" : ""+ ClientID +"", "Authorization": "oauth:" + Token}
    response = requests.get(url, headers=params).json()
    StreamStart = response['data'][0]
    # print response
    # returns
    # {u'pagination': {u'cursor': u'eyJiIjpudWxsLCJhIjp7Ik9mZnNldCI6MX19'}, u'data': [{
        # u'user_id': u'109949586',
        # u'language': u'',
        # u'title': u'This is the title',
        # u'type': u'live',
        # u'tag_ids': None,
        # u'community_ids': [],
        # u'thumbnail_url': u'https://static-cdn.jtvnw.net/previews-ttv/live_user_riboture-{width}x{height}.jpg',
        # u'game_id': u'0',
        # u'started_at': u'2018-11-16T11:04:29Z',
        # u'user_name': u'',
        # u'id': u'31261236144',
        # u'viewer_count': 0}
    # ]}
    m = re.search('T(.+?):', StreamStart['started_at'])
    startHours = m.group(1)
    m = re.search(':(.+?):', StreamStart['started_at'])
    startMinutes = m.group(1)
    finishTime = datetime.datetime.utcnow().strftime("%H:%M")
    m = re.search('(.+?):', finishTime)
    finishHours = m.group(1)
    m = re.search(':(.*)', finishTime)
    finishMinutes = m.group(1)
    totalStartMinutes = (int(startHours) * 60) + int(startMinutes)
    totalFinishMinutes = (int(finishHours) * 60) + int(finishMinutes)
    m = re.search('(.+?)T', StreamStart['started_at'])
    startDate = m.group(1).encode('ascii', 'ignore')
    m = re.search('(.+?)-', startDate)
    startYear = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.+?)-', startDate)
    startMonth = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', startDate)
    startDay = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', startDay)
    startDay = m.group(1).encode('ascii', 'ignore')
    finishDate = str(datetime.datetime.utcnow().strftime("%Y-%m-%d"))
    m = re.search('(.+?)-', finishDate)
    finishYear = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.+?)-', finishDate)
    finishMonth = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', finishDate)
    finishDay = m.group(1).encode('ascii', 'ignore')
    m = re.search('-(.*)', finishDay)
    finishDay = m.group(1).encode('ascii', 'ignore')
    d1 = datetime.date(int(startYear), int(startMonth), int(startDay))
    d2 = datetime.date(int(finishYear), int(finishMonth), int(finishDay))
    delta = d2 - d1
    if delta.days == 1:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (24 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 2:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (48 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 3:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes) + (72 * 60)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"
    if delta.days == 0:
        totalUptimeMinutes = int(totalFinishMinutes) - int(totalStartMinutes)
        uptimeHours = int(math.floor(totalUptimeMinutes / 60))
        uptimeMinutes = totalUptimeMinutes - (uptimeHours * 60)
        return "The stream has been live for " + str(uptimeHours) + "h " + str(uptimeMinutes) + "m"

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

while True:

    try:
        def message(msg):
            try:
                s.send("PRIVMSG " + Channel + " :" + msg + "\n")
            except IndexError:
                pass
        response = s.recv(1024).decode("utf-8")
        data = response.strip("\r\n")
        if True == True:
            try:
                # Get new follower list and format it to compare with unfollowers
                followers()
                test = []
                for i in range(len(followerList)):
                    test.insert(0, followerList[i]['from_name'].encode('ascii', 'ignore'))
                test = map(str.strip, test)

                # Get existing follower list
                if not os.path.exists('followerData.csv'):
                    open('followerData.csv', "w+").close()
                with open('followerData.csv', "rb") as csvfile:
                    followerDataReader = csv.reader(csvfile, delimiter=",")
                    lines = list(followerDataReader)

                # Compare follower lists
                newFollowers = [item for item in test if item not in [i[0] for i in lines[1:]]]
                unfollowers = [item for item in [i[0] for i in lines[1:]] if item not in test]

                # thank new follower and add to existing list
                if len(newFollowers) > 0:
                    if len(lines) == 0:
                        lines.append(
                            ["Username", "FollowLength", "IsFollower", "BatName", "BatGender", "BatColor", "IsSubscriber"])
                    for i in range(len(newFollowers)):
                        lines.append([newFollowers[i], "", "", "", "", "", ""])
                    with open('followerDataNew.csv', "wb") as csvfile:
                        followerDataWriter = csv.writer(csvfile, delimiter=",")
                        followerDataWriter.writerows(lines)
                    os.remove('followerData.csv')
                    os.rename('followerDataNew.csv', 'followerData.csv')
                    if len(newFollowers) == 1:
                        message("Thank you for following the channel " + " ".join(newFollowers) + "! Type !bat to see your bat's information")
                    if len(newFollowers) > 1:
                        message("Thank you for following the channel " + ", ".join(newFollowers[0:-1]) + " and " + newFollowers[-1] + "! Type !bat to see your bat's information")

                # If someone unfollows set follow value to 0
                for i1 in range(len(unfollowers)):
                    for i2 in range(len(lines)):
                        if lines[i2][0] == unfollowers[i1]:
                            lines[i2][2] = "0"
                # If someone follows set follow value to 1
                for i1 in range(len(lines)):
                    for i2 in range(len(followerList)):
                        if lines[i1][0] == followerList[i2]['from_name'].rstrip():
                            lines[i1][2] = "1"

                # Assign gender
                for i in range(len(lines)):
                    if lines[i][4] == "":
                        maleFemale = random.randint(0, 1)
                        if maleFemale == 1:
                            lines[i][4] = 'Female'
                        else:
                            lines[i][4] = 'Male'

                # Assign Name
                for i in range(len(lines)):
                    try:
                        if lines[i][3] == "":
                            if lines[i][4] == 'Male':
                                randomNumber = random.randint(0, len(batMaleNames))
                                maleName = batMaleNames[randomNumber]
                                lines[i][3] = maleName
                            if lines[i][4] == 'Female':
                                randomNumber = random.randint(0, len(batFemaleNames))
                                femaleName = batFemaleNames[randomNumber]
                                lines[i][3] = femaleName
                    except IndexError:
                        print 'Skipped adding gender. Will add next time this loops'
                        pass

                # Refresh the total seconds followed per user
                followAgeAll()
                for i in range(len(lines)):
                    for i2 in range(len(followerList)):
                        if lines[i][0] == followerList[i2]['from_name'].rstrip():
                            lines[i][1] = followAgeList[i2][5]

                # Assign color
                global totalBlackBats, totalBrownBats, totalRedBats
                global blackBatScore, brownBatScore, redBatScore
                global percentageBlackBats, percentageRedBats, percentageBrownBrownBats
                global totalColoredBats
                totalColoredBats = 0.00
                totalBlackBats = 0.00
                totalBrownBats = 0.00
                totalRedBats = 0.00
                if lines[1][5] == "":
                    lines[1][5] = 'Black'
                if lines[2][5] == "":
                    lines[2][5] = 'Brown'
                if lines[3][5] == "":
                    lines[3][5] = 'Red'
                try:
                    for i in range(len(lines)):

                        if totalColoredBats > 2:
                            percentageBlackBats = float(totalBlackBats / totalColoredBats)
                            percentageBrownBats = float(totalBrownBats / totalColoredBats)
                            percentageRedBats = float(totalRedBats / totalColoredBats)

                            blackBatScore = 0.6 - percentageBlackBats
                            brownBatScore = 0.3 - percentageBrownBats
                            redBatScore = 0.1 - percentageRedBats

                            # see if list is empty and add value
                            try:
                                if lines[i][5] == "":
                                    if (blackBatScore > brownBatScore) and (blackBatScore > redBatScore):
                                        lines[i][5] = 'Black'
                                    if (blackBatScore > brownBatScore) and (blackBatScore == redBatScore):
                                        lines[i][5] = 'Black'
                                    if (brownBatScore > blackBatScore) and (brownBatScore > redBatScore):
                                        lines[i][5] = 'Brown'
                                    if (brownBatScore > blackBatScore) and (brownBatScore == redBatScore):
                                        lines[i][5] = 'Brown'
                                    if (redBatScore > blackBatScore) and (redBatScore > brownBatScore):
                                        lines[i][5] = 'Red'
                                    if (redBatScore > blackBatScore) and (redBatScore == brownBatScore):
                                        lines[i][5] = 'Red'
                                    if (blackBatScore == brownBatScore) and (brownBatScore == redBatScore):
                                        lines[i][5] = 'Black'
                            except Exception, e:
                                print "could not decide bat color"
                                print(str(e))

                        # check for which bat to add next
                        if lines[i][5] == 'Black':
                            totalBlackBats = totalBlackBats + 1
                        if lines[i][5] == 'Brown':
                            totalBrownBats = totalBrownBats + 1
                        if lines[i][5] == 'Red':
                            totalRedBats = totalRedBats + 1
                        totalColoredBats = totalBlackBats + totalBrownBats + totalRedBats

                except IndexError:
                    pass
                except Exception, e:
                    print "could not add bat color"
                    print (str(e))

                # Check if subscriber or not.
                subscribers()
                for i1 in range(len(lines)):
                    lines[i1][6] = 0
                for i1 in range(len(lines)):
                    for i2 in range(len(subscriberResponse['subscriptions'])):
                        if lines[i1][0].lower() == subscriberResponse['subscriptions'][i2]['user']['display_name'].lower():
                            lines[i1][6] = 1


                # After all the editing has been done write back all the lines
                # I had to write back to a new file and rename it because of lack of memory

                if not os.path.exists('followerDataNew.csv'):
                    open('followerDataNew.csv', "w+").close()
                with open('followerDataNew.csv', "wb") as csvfile:
                    followerDataWriter = csv.writer(csvfile, delimiter=",")
                    followerDataWriter.writerows(lines)
                os.remove('followerData.csv')
                os.rename('followerDataNew.csv', 'followerData.csv')

                # open the subsciber file to get the lines to the Sub file
                if not os.path.exists('subscriberData.csv'):
                    open('subscriberData.csv', "w+").close()
                global subscriberLines
                with open('subscriberData.csv', "rb") as csvfile:
                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                    subscriberLines = list(subscriberDataReader)

                subscriberList = []
                for i in range(len(subscriberResponse['subscriptions'])):
                    subscriberList.insert(0, subscriberResponse['subscriptions'][i]['user']['display_name'].encode('ascii', 'ignore'))
                subscriberList = map(str.strip, subscriberList)

                newSubscribers = [item for item in subscriberList if item not in [i[0] for i in subscriberLines[1:]]]
                newGiftedSubscribers = []
                newGifters = []
                newSelfSubscribers = []
                for i1 in range(len(newSubscribers)):
                        for i2 in range(len(subscriberResponse['subscriptions'])):
                            subscriberName = subscriberResponse['subscriptions'][i2]['user']['display_name'].lower()
                            if subscriberName == newSubscribers[i1].lower():
                                if subscriberResponse['subscriptions'][i2]['is_gift'] == False:
                                    newSelfSubscribers.append(newSubscribers[i1])
                                if subscriberResponse['subscriptions'][i2]['is_gift'] == True:
                                    newGiftedSubscribers.append(newSubscribers[i1])
                                    newGifters.append(subscriberResponse['subscriptions'][i2]['sender'].encode('ascii', 'ignore'))

                unSubscribers = [item for item in [i[0] for i in subscriberLines[1:]] if item not in subscriberList]

                if len(newSubscribers) > 0:
                    if len(subscriberLines) == 0:
                        subscriberLines.append(
                            ["Username", "SubStreak", "SubTier", "Elf1", "ElfGender1", "Elf2", "ElfGender2", "Elf3",
                             "ElfGender3", "Elf4", "ElfGender4", "Elf5", "ElfGender5", "Elf6", "ElfGender6", "LastName",
                             "IsSubscriber"])
                    for i1 in range(len(newSubscribers)):
                        subscriberLines.append([newSubscribers[i1]] + ([""] * 16))
                    if len(newSelfSubscribers) == 1:
                        message("Thank you for subscribing" + " ".join(newSelfSubscribers) + "! Type !elf to see your elf's information")
                    if len(newSelfSubscribers) > 1:
                        message("Thank you for the subscriptions " + ", ".join(newSelfSubscribers[0:-1]) + " and " + newSelfSubscribers[-1] + "! Type !elf to see your elf's information")
                    if len(newGiftedSubscribers) == 1:
                        message(newGifters + " has given a subscription to " + " ".join(newGiftedSubscribers) + "! Type !elf to see your elf's information")
                    if len(newGifters) == 1:
                        if len(newGiftedSubscribers) > 1:
                            message(" ".join(newGifters) + "Has gifted a sub to the lucky " + ", ".join(newGiftedSubscribers[0:-1]) + " and " + newGiftedSubscribers[-1] + "! Type !elf to see your elf's information")
                    if len(newGifters) > 1:
                        if len(newGiftedSubscribers) > 1:
                            message(" ".join(newGifters) + "have gifted " + str(
                                len(newGiftedSubscribers)) + " subs in total to the lucky " + ", ".join(
                                newGiftedSubscribers[0:-1]) + " and " + newGiftedSubscribers[
                                        -1] + "! Type !elf to see your elf's information")

                # Thank for upgrading and set Subtier
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscriberResponse['subscriptions'])):
                        if subscriberResponse['subscriptions'][i2]['user']['display_name'].encode('ascii', 'ignore') == subscriberLines[i1][0]:
                            # Check for upgrades of existing subscriptions
                            if subscriberResponse['subscriptions'][i2]['sub_plan'][0] > subscriberLines[i1][2]:
                                if subscriberResponse['subscriptions'][i2]['sub_plan'] == u'2000':
                                    message("Thank you " + subscriberResponse['subscriptions'][i2]['user']['display_name'].encode('ascii', 'ignore') + "for upgrading your subscription to tier 2!")
                                if subscriberResponse['subscriptions'][i2]['sub_plan'] == u'3000':
                                    message("Thank you " + subscriberResponse['subscriptions'][i2]['user']['display_name'].encode('ascii', 'ignore') + " for upgrading your subscription to tier 3!")

                            # Set sub tier
                            subscriberLines[i1][2] = subscriberResponse['subscriptions'][i2]['sub_plan'].encode('ascii', 'ignore')
                            subscriberLines[i1][2] = subscriberLines[i1][2][0]

                # Assign gender
                for i1 in range(len(subscriberLines)):
                    if subscriberLines[i1][2] == "1":
                        if subscriberLines[i1][4] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][4] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][4] = 'Male'
                    if subscriberLines[i1][2] == "2":
                        if subscriberLines[i1][4] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][4] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][4] = 'Male'
                        if subscriberLines[i1][6] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][6] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][6] = 'Male'
                    if subscriberLines[i1][2] == "3":
                        if subscriberLines[i1][4] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][4] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][4] = 'Male'
                        if subscriberLines[i1][6] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][6] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][6] = 'Male'
                        if subscriberLines[i1][8] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][8] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][8] = 'Male'
                        if subscriberLines[i1][10] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][10] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][10] = 'Male'
                        if subscriberLines[i1][12] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][12] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][12] = 'Male'
                        if subscriberLines[i1][14] == "":
                            maleFemale = random.randint(0, 2)
                            if maleFemale == 1:
                                subscriberLines[i1][14] = 'Female'
                            if maleFemale == 2:
                                subscriberLines[i1][4] = 'Androgynous'
                            else:
                                subscriberLines[i1][14] = 'Male'

                # Assign first and last name
                for i in range(len(subscriberLines)):
                    try:
                        if subscriberLines[i][2] == "1":
                            if subscriberLines[i][3] == "":
                                if subscriberLines[i][4] == 'Male':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][3] = maleName
                                if subscriberLines[i][4] == 'Female':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][3] = femaleName
                                if subscriberLines[i][4] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][3] = androgynousName
                        if subscriberLines[i][2] == "2":
                            if subscriberLines[i][3] == "":
                                if subscriberLines[i][4] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][3] = maleName
                                if subscriberLines[i][4] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][3] = femaleName
                                if subscriberLines[i][4] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][3] = androgynousName
                            if subscriberLines[i][5] == "":
                                if subscriberLines[i][6] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][5] = maleName
                                if subscriberLines[i][6] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][5] = femaleName
                                if subscriberLines[i][6] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][5] = androgynousName
                        if subscriberLines[i][2] == "3":
                            if subscriberLines[i][3] == "":
                                if subscriberLines[i][4] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][3] = maleName
                                if subscriberLines[i][4] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][3] = femaleName
                                if subscriberLines[i][4] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][3] = androgynousName
                            if subscriberLines[i][5] == "":
                                if subscriberLines[i][6] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][5] = maleName
                                if subscriberLines[i][6] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][5] = femaleName
                                if subscriberLines[i][6] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][5] = androgynousName
                            if subscriberLines[i][7] == "":
                                if subscriberLines[i][8] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][7] = maleName
                                if subscriberLines[i][8] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][7] = femaleName
                                if subscriberLines[i][8] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][7] = androgynousName
                            if subscriberLines[i][9] == "":
                                if subscriberLines[i][10] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][9] = maleName
                                if subscriberLines[i][10] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][9] = femaleName
                                if subscriberLines[i][10] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][9] = androgynousName
                            if subscriberLines[i][11] == "":
                                if subscriberLines[i][12] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][11] = maleName
                                if subscriberLines[i][12] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][11] = femaleName
                                if subscriberLines[i][12] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][11] = androgynousName
                            if subscriberLines[i][13] == "":
                                if subscriberLines[i][14] == 'Male':
                                    randomNumber = random.randint(0, len(elfNameMale))
                                    maleName = elfNameMale[randomNumber]
                                    subscriberLines[i][13] = maleName
                                if subscriberLines[i][14] == 'Female':
                                    randomNumber = random.randint(0, len(elfNamesFemale))
                                    femaleName = elfNamesFemale[randomNumber]
                                    subscriberLines[i][13] = femaleName
                                if subscriberLines[i][14] == 'Androgynous':
                                    randomNumber = random.randint(0, len(elfNameAndrogynous))
                                    androgynousName = elfNameAndrogynous[randomNumber]
                                    subscriberLines[i][13] = androgynousName
                        if subscriberLines[i][15] == "":
                            randomNumber = random.randint(0, len(elfLastNames))
                            elfLastName = elfLastNames[randomNumber]
                            subscriberLines[i][15] = elfLastName
                    except IndexError:
                        print 'Skipped adding elf name or gender. Will add next time this loops'
                        pass

                # Check if subscriber or not.
                for i1 in range(len(subscriberLines)):
                    if not subscriberLines[i1][16] == "IsSubscriber":
                        subscriberLines[i1][16] = 0
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscriberResponse['subscriptions'])):
                        if subscriberLines[i1][0].lower() == subscriberResponse['subscriptions'][i2]['user']['display_name'].lower():
                            subscriberLines[i1][16] = 1

                # Add length since subscription
                subscribeAgeAll()
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscribeAgeList)):
                        if not subscriberLines[i1][1] == "SubStreak":
                            subscriberName = subscribeAgeList[i2][8].lower()
                            if subscriberLines[i1][0].lower() == subscriberName.encode('ascii', 'ignore'):
                                subscriberLines[i1][1] = subscribeAgeList[i2][7]

                # write back any changes to a the subscriber file
                with open('subscriberDataNew.csv', "wb") as csvfile:
                    subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                    subscriberDataWriter.writerows(subscriberLines)
                os.remove('subscriberData.csv')
                os.rename('subscriberDataNew.csv', 'subscriberData.csv')

            except IndexError:
                pass
            except Exception, e:
                print("while true events error")
                print(str(e))
        if response == "PING :tmi.twitch.tv\r\n":
            try:
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            except IndexError:
                 pass
        if "!commands" in data.lower().split()[3]:
            try:
                message("See what the bot can do here: https://github.com/ridgure/twitchbot#features")
            except IndexError:
                pass
        if "!test" in data.lower().split()[3]:
            try:
                subscribers()
                message(subscribeAgeAll())
            except IndexError:
                pass
            except Exception, e:
                message("Division failed")
                message(str(e))
        if "!social" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: fb.com/Ridgure")
                message("Add me on Twitter: Twitter.com/RigidStructure")
                message("Add me on Instagram: Instagram.com/Ridgure")
            except IndexError:
                pass
        if "!facebook" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: fb.com/Ridgure")
            except IndexError:
                pass
        if "!twitter" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: Twitter.com/RigidStructure")
            except IndexError:
                pass
        if "!instagram" in data.lower().split()[3]:
            try:
                message("Add me on Facebook: Instagram.com/RigidStructure")
            except IndexError:
                pass
        if "!bat" in data.lower().split()[3]:
            try:
                batInfo = None
                if len(data.lower().split()) == 5:
                    for i in range(len(lines)):
                        if lines[i][0].lower() == data.lower().split()[4]:
                            batInfo = lines[i]
                    if batInfo == None:
                        message("User is not following the channel")
                    if batInfo[4] == 'Male':
                        gender = 'He'
                    if batInfo[4] == 'Female':
                        gender = 'She'
                    message(data.split()[4] + "'s bat is called " + batInfo[3] + ". " + gender + " is colored " + batInfo[5].lower())
                if not len(data.lower().split()) == 4:
                    for i in range(len(lines)):
                        if lines[i][0] == sender():
                            batInfo = lines[i]
                    if batInfo[4] == 'Male':
                        gender = 'He'
                    if batInfo[4] == 'Female':
                        gender = 'She'
                    message("Your bat is called " + batInfo[3] + ". " + gender + " is colored " + batInfo[5].lower())
            except IndexError:
                pass
            except Exception, e:
                pass
        if "!elf" in data.lower().split()[3]:
            try:
                elfInfo = None
                if len(data.lower().split()) == 5:
                    for i in range(len(subscriberLines)):
                        if subscriberLines[i][0].lower() == data.lower().split()[4]:
                            elfInfo = subscriberLines[i]
                    if elfInfo == None:
                        message("User is not a subscriber")
                    if elfInfo[4] == 'Male':
                        gender = 'His'
                    if elfInfo[4] == 'Female':
                        gender = 'Her'
                    if elfInfo[4] == 'Androgynous':
                        gender = 'Their'
                    if elfInfo[2] == "1":
                        message(
                            data.split()[4] + "'s bat morphed into 1 elf. " + gender + " name is " + elfInfo[3] + " " +
                            elfInfo[15])
                    if elfInfo[2] == "2":
                        message(
                            data.split()[4] + "'s bat morphed into 2 elves. Their names are " + elfInfo[3] + " and " +
                            elfInfo[5] + " " + elfInfo[15])
                    if elfInfo[2] == "3":
                        message(
                            data.split()[4] + "'s bat morphed into 6 elves. Their names are " + elfInfo[3] + ", " +
                            elfInfo[5] + ", " + elfInfo[7] + ", " + elfInfo[9] + ", " + elfInfo[11] + " and " + elfInfo[
                                13] + " " + elfInfo[15])
                if len(data.lower().split()) == 4:
                    "test 0"
                    for i in range(len(subscriberLines)):
                        "test 1"
                        if subscriberLines[i][0].lower() == sender():
                            "test 2"
                            elfInfo = subscriberLines[i]
                    if elfInfo[4] == 'Male':
                        gender = 'His'
                    if elfInfo[4] == 'Female':
                        gender = 'Her'
                    if elfInfo[4] == 'Androgynous':
                        gender = 'Their'
                    if elfInfo[2] == "1":
                        message(
                            "Your bat morphed into 1 elf. " + gender + " name is " + elfInfo[3] + " " + elfInfo[15])
                    if elfInfo[2] == "2":
                        message(
                            "Your bat morphed into 2 elves. Their names are " + elfInfo[3] + " and " +
                            elfInfo[5] + " " + elfInfo[15])
                    if elfInfo[2] == "3":
                        message(
                            "Your bat morphed into 6 elves. Their names are " + elfInfo[3] + ", " +
                            elfInfo[5] + ", " + elfInfo[7] + ", " + elfInfo[9] + ", " + elfInfo[11] + " and " + elfInfo[
                                13] + " " + elfInfo[15])
            except IndexError, e:
                print str(e)
                pass
            except Exception, e:
                print str(e)
                pass
        if "!raid" in data.lower().split()[3]:
            try:
                if sender().lower() == Channel[1:]:
                    message("Please raid Twitch.tv/" + data.split()[4] + " msg: Ridgure raid twitchRaid twitchRaid twitchRaid")
                else:
                    pass
            except IndexError:
                pass
        if "!pack" in data.lower().split()[3]:
            try:
                message("The modpack I am playing is called FTB Infinity Evolved on expert mode. Minecraft version 1.7.10. It is available through the twitch launcher and on curse")
            except IndexError:
                pass
        if "!oclock" in data.lower().split()[3]:
            try:
                message("The time for me right now is " + datetime.datetime.now().strftime("%H:%M") + " o'clock" + " CET")
            except IndexError:
                pass
        if "!shout" in data.lower().split()[3]:
            try:
                message("Check out this awesome streamer over at Twitch.tv/" + data.split()[4])
            except IndexError:
                pass
        if "!lick" in data.lower().split()[3]:
            try:
                if sender() == 'pupgirl22':
                    message(sender() + " licks " + data.split()[4] + lick())
                else:
                    pass
            except IndexError:
                pass
        if "!bellyrub" in data.lower().split()[3]:
            try:
                message(sender() + " rubs " + data.split()[4] + "'s belly " + lick())
            except IndexError:
                pass
        if "cobble" in data.lower().split()[2:]:
            try:
                message("Eww not cobble!")
            except IndexError:
                pass
        if "!batnamechange" in data.lower().split()[3]:
            try:
                with open('followerData.csv', "rb") as csvfile:
                    followerDataReader = csv.reader(csvfile, delimiter=",")
                    lines = list(followerDataReader)

                for i in range(len(lines)):
                    if lines[i][0] == sender():
                        lines[i][3] = data.split(4)
                        message("Successfully changed the name of " + sender() + "'s bat to: " + data.split()[4])

                with open('followerDataNew.csv', "wb") as csvfile:
                    followerDataWriter = csv.writer(csvfile, delimiter=",")
                    followerDataWriter.writerows(lines)
                os.remove('followerData.csv')
                os.rename('followerDataNew.csv', 'followerData.csv')

            except IndexError:
                pass
        if "!timemeout" in data.lower().split()[3]:
            try:
                ## time out KBiglair ##
                if 0 < int(data.split()[4]) < 3601:
                    message("/timeout " + sender() + " " + data.split()[4])
                    message("Timed out " + sender() + " for " + data.split()[4] + " seconds")
                elif int(data.split()[4]) < 0:
                    message("You cannot go back in time unless you are the doctor or Marty McFly")
                else:
                    message("TimeMeOut failed")
            except IndexError:
                message("Add amount of seconds you want to be timed out after command")
                pass
        if "!uptime" in data.lower().split()[3]:
            try:
                message(uptime())
            except IndexError:
                print "Uptime failed"
        if "!fc" in data.lower().split()[3]:
            try:
                # get the user
                if len(data.lower().split()) == 4:
                    user = sender()
                if len(data.lower().split()) == 5:
                    user = (data.lower().split()[4])

                testFollower = False
                # get user index and get their follow time and date and length
                for i1 in xrange(len(followerList)):
                    for i2 in xrange(len(followerList[i1])):
                        # print i1, followerList[i1]['from_name']
                        if followerList[i1]['from_name'].lower() == user:
                            followAge = followAgeAll()
                            message("Last follow was on: " + str(
                                followAge[i1][6]) + " GMT-0 and has been following the channel for " + str(
                                followAge[i1][1]) + " days, " + str(followAge[i1][2]) + " hours, " + str(
                                followAge[i1][3]) + " minutes and " + str(followAge[i1][4]) + " seconds")
                            user = None
                            testFollower = True
                        else:
                            pass
                if testFollower == False:
                    message("User is not following the channel")

            except IndexError:
                pass
            except Exception, e:
                message("followage failed")
                message(str(e))
        if "!elfnamechange" in data.lower().split()[3]:
            try:
                owner = False
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscriberLines[i1])):
                        if subscriberLines[i1][0].lower() == sender().lower():
                            if data.lower().split()[4] == subscriberLines[i1][i2].lower():
                                with open('subscriberData.csv', "rb") as csvfile:
                                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                                    subscriberLines = list(subscriberDataReader)
                                subscriberLines[i1][i2] = data.split()[7]
                                subscriberLines[i1][15] = data.split()[8]
                                message("Successfully changed the name of " + data.split()[4] + " " + data.split()[
                                        5] + " to " + data.split()[7] + " " + subscriberLines[i1][15])
                                with open('subscriberDataNew.csv', "wb") as csvfile:
                                    subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                                    subscriberDataWriter.writerows(subscriberLines)
                                os.remove('subscriberData.csv')
                                os.rename('subscriberDataNew.csv', 'subscriberData.csv')
                                owner = True
                if owner == False:
                    message("You cannot change the name of other people's elves")
            except IndexError:
                message("Did you remember to write '!elfnamechange firstName lastname to first name lastname'?")
                print "elfnamechange failed"
        if "!elfgenderchange" in data.lower().split()[3]:
            try:
                owner = False
                for i1 in range(len(subscriberLines)):
                    for i2 in range(len(subscriberLines[i1])):
                        if subscriberLines[i1][0].lower() == sender().lower():
                            if data.lower().split()[4] == subscriberLines[i1][i2].lower():
                                with open('subscriberData.csv', "rb") as csvfile:
                                    subscriberDataReader = csv.reader(csvfile, delimiter=",")
                                    subscriberLines = list(subscriberDataReader)
                                genderIndex = (int(i2) + 1)
                                if data.split()[6] == "Male" or data.split()[6] == "Female" or data.split()[6] == "Androgynous":
                                    message("Successfully changed the gender of " + subscriberLines[i1][i2] + " from " +
                                            subscriberLines[i1][genderIndex] + " to " + data.split()[6])
                                    subscriberLines[i1][genderIndex] = data.split()[6]
                                else:
                                    message("The gender can only be Male, Female or Androgynous")
                                with open('subscriberDataNew.csv', "wb") as csvfile:
                                    subscriberDataWriter = csv.writer(csvfile, delimiter=",")
                                    subscriberDataWriter.writerows(subscriberLines)
                                os.remove('subscriberData.csv')
                                os.rename('subscriberDataNew.csv', 'subscriberData.csv')
                                owner = True
                if owner == False:
                    message("You cannot change the gender of other people's elves")
            except IndexError:
                message("Did you remember to write '!elfgenderchange firstName to gender'?")
                print "elfnamechange failed"
        if "!smile" in data.lower().split()[3]:
            try:
                message(sender() + " smiles at " + data.split()[4] + " " + randomEmote())
            except IndexError:
                message("Remember to smile at someone!")
            except Exception, e:
                message("Smile failed")
                message(str(e))
        if "!multiply" in data.lower().split()[3]:
            try:
                message(multiply())
            except IndexError:
                pass
            except Exception, e:
                message("Multiplication failed")
                message(str(e))
        if "!divide" in data.lower().split()[3]:
            try:
                message(divide())
            except IndexError:
                pass
            except Exception, e:
                message("Division failed")
                message(str(e))
        if "!add" in data.lower().split()[3]:
            try:
                message(add())
            except IndexError:
                pass
            except Exception, e:
                message("Addition failed")
                message(str(e))
        else:
            username = re.search(r"\w+", response).group(0) # return the entire match
            message = CHAT_MSG.sub("", response)
            try:
                f = open("output.txt", "a")
                f.write(username + ": " + message)
                f.close()
                f = open("output.txt", "r")
                lines = f.readlines()
                f.close()
                f = open("output.txt", "w")
                displayedLines = 20
                if len(lines) > displayedLines:
                    backlog = len(lines) - displayedLines
                    f.truncate()
                    f.writelines(lines[backlog:len(lines)])
                    f.close()
                else:
                    f.writelines(lines)
                    f.close()
            except:
                pass
            print(username + ": " + message)
###            print response
            sleep(0.1)
    except IndexError:
        pass
    except Exception, e:
        print "An error just occurred"
        print str(e)
