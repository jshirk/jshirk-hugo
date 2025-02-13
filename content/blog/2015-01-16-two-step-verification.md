---
title: Increasing Digital Security with Two-Step Verification
author: Jordan Shirkman
type: post
date: 2015-01-16T10:00:33+00:00
url: /two-step-verification/
categories:
  - Technology

---
_Before you get into this post, know that it’s a 2,400+ word labor of love. This stuff is tricky for me to explain, but I cannot overemphasize how important it is, and that’s why you’re reading a preface to a blog post. The few minutes it’ll take to read this post and the 20-minute process of setting up 2-step verification is worth it. At the bottom of this post you’ll see all the links you need to get started._

I’ve written about the [need](https://jshirk.com/blog/1password/) for serious security in our digital lives. It’s too easy for thieves to swipe passwords, bank account numbers, and critical information that could create a crapstorm of chaos, frustration, and loss for us.

![Image](/static/images/locks.jpeg) 

**Fortunately, there’s an added layer of security that’s equivalent to bringing your toughest friend to back you up in a schoolyard brawl. It’s called 2-step verification (2SV) or sometimes two-factor authentication**.

**Basically, as well as having a password to sign into an account, you need a second device which gives you code–essentially verifying your identity–as well.** It’s like providing two forms of ID when you get a driver’s license–a social-security card plus a birth certificate. It greatly reduces the chances of criminals accessing your accounts because they have to have _two things_ only you should have–your password _and_ your phone.

2SV means hackers need more than your password to access your accounts when you sign in from an “unknown” device[footnote]An internet-connected device you haven’t logged into that service with before[/footnote]. With a strong password and 2SV, there’s a great chance dirtballs are going to give up on you and try to steal from an easier target.

## Two Ways 2SV Works

There are two main ways 2SV validates that you are who you say you are. It still starts with you entering your password, but then the service **either sends you 1. a text message with a new code every time you want to login on a new device, or 2. enables you to use an app called a code generator to create time-sensitive codes for you to enter when you login.**

The good news is that you don’t have to use 2SV every time you signin–only when you’re on a new device. So the hassle is minimal and totally worth it for the security enhancements.

### 1. The Text-Message Option

A text message 2SV is simple–when you set up 2SV on your account, the service will ask for your cell phone number, you plop it in, get a text, and then punch in the 4- to 6-digit code they sent to you.

That’s how it’ll work every time. I find this way a bit restricting because you **always** to have your phone with you.[footnote]As opposed to being able to use another device, like an iPod or iPad[/footnote] If you travel abroad often or don’t always have cell phone service (for our backwoods blog readers), it can really cramp your style. You could also be charged for text message fees while abroad if you’re a globetrotter.

Not all country phone numbers are supported, so unless your Uncle is Sam, you may not even be able to enable this option. Also, if your phone is stolen, you’ll be forced to use your recovery code (more on that soon), so you have fewer options with this method. [footnote]Like a true 20-something, I detest this method because it doesn’t allow me to “keep my options open.”[/footnote]

### 2. The (Better) Code-Generation Option

The second option is a code generator. You download a code-generating app like [Authy](https://itunes.apple.com/us/app/authy/id494168017?mt=8&at=11l4uNett), my app of choice, or [Google Authenticator](https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8&at=11l4uNett), then you login to the service where you’ve enabled 2SV and choose generate a code.

Once you’ve set up your account in Authy, you’ll login to the service you want to have Authy generate codes for–e.g. Gmail or Evernote. Then, in the 2SV-option section, choose something like “code generator.” The site will bring up a QR code[footnote]Perhaps the only valid use-case for those funny squares [/footnote] that you’ll scan, linking your account to the app, and voilà, you’re up and running with 2SV. Anytime you need a code for that service, just open the Authy app. It’s faster and easier than a text message, and you can use it anytime you have an Internet connection.

You can set up multiple services this way with Authy, so I have my Evernote, Dropbox, and Gmail accounts all in one place. **That makes Authy a one-stop, code-generating shop.**

I prefer Authy because you can login to the app on multiple devices, so you can have the same codes generated on your iPad and iPhone. I’m not sure how to get Google Authenticator working on multiple devices, so that’s why I prefer Authy–it syncs automatically if you create an Authy account (and the app guides you through that process). That means whatever device you have handy will work. Be sure to save the Authy backup code saved somewhere (like 1Password), which allows you to access Authy from a new device if your other devices are lost are stolen.

## Best Practices

2SV can get overly complicated quickly. Here’s what I would focus on.

### 1. Save your recovery code

When you setup 2SV, each service will give you a **super-duper important recovery code** that is your get-out-of-jail-free card if you happen to lose your device that you generates your one-time authentication codes.

You absolutely, 100% _must_ have a system for organizing these **one-time**, single bullet in the chamber, use it or lose everything, **recovery codes** in case you lose the devices with which you have your account setup.

Each service will give you at least one recovery code (e.g. Apple and Dropbox) or sometimes 4 to 10 (e.g. Evernote, Google). **No one can save you, not even Jesus, from being permanently locked out of your account without this code if you lose your primary devices where you’re already signed in.** So, if your phone is stolen and that was the only place you had your backup codes saved (not a good idea), you’re cooked and permanently locked out of every important thing you have in those accounts. Goodbye Evernotes, Dropbox files, emails and apps.

I cannot possibly strike into you the fear-of-God about losing your recovery code enough. I have mine saved in 1Password, my wife has a copy in her 1Password, and I have another secret place I keep my codes. [footnote]I’d tell you where, but then it wouldn’t be a secret.[/footnote] I’m that nerdy and that serious about security and not losing everything. I would even consider getting a safe deposit box at a bank to put the codes in if I knew how to do that in Slovenia.

### 2. Use 1Password and make your life easier

[1Password](https://jshirk.com/blog/1password) makes saving your one-time recovery codes a cakewalk–just save your recovery code under your login details for whatever app you’ve enabled 2SV with, like this:

![Image](/static/images/Google-Codes-Screenshot.jpeg) 

I wouldn’t recommend going with 2SV route without a solid password manager, like 1Password. It might be a good idea to give your recovery codes to a spouse or trusted relative to hold onto. If you print them out, as many services suggest, and your house burns down with all of your codes and devices, you’ve increased your nightmare.

If you’re using Dropbox to sync your 1Password across devices LINK, 1Password has a pretty amazing feature where you can access your information anywhere you login to Dropbox. Just open _1Password.agilekeychain_, then the _1Password.html_ file. That will bring up a version of 1Password that runs in your browser where you can type in your Master Password, and then access all of your account information. Incredibly handy if you’re using someone else’s computer but still need your passwords.

**As long as you can login to your Dropbox account, you can get to your other codes and information. That means your single Dropbox recovery code is the golden ticket of this entire system.** So tattoo that code to your inner thigh, print it out and stick it between your insole and shoe, or fold it up nice and tiny and stick it just inside your left ear. Just don’t tell us which option you choose (we won’t judge if you stray away from the tattoo option).

### 3. Be organized

2SV adds an additional burden to users, but it’s worth it for the extra security. You have to be organized. Now you have to know your main password, and have a way to get a code (via text or app). If you don’t use a password manager, which, come on, I’ve already beat that drum and we know it is a huge mistake, you better be so organized you can appropriate dust mites in your sleep.

A password manager is worth the investment, but if you don’t go that route, you better have A-Beautiful-Mind-like brain where your store all of these strong, unique passwords and recovery codes.

### 4. Be patient

2SV is a bit cumbersome and confusing. That is, unfortunately, the reality of living on planet earth post-Garden-of-Eden. 90% of the time, you’ll never have to use a code generator once you set it up.

It’s frustrating that every service has a slightly different process for setting up 2SV as well. I wish there was a streamlined way to say, “Just do this and you’re good to go,” but it’s not that simple.

For example, you can use a code generator with Google, Evernote and Dropbox, but Apple requires you use a cell phone and receive a text message, or get a notification that they push through to one of your iOS devices.[footnote]Maybe I’m missing something, but I don’t think there is a way to get these codes on a Mac, which is frustrating and a bit confusing. My guess is that if your laptop gets snatched, no one can just log into your accounts, especially if you save your passwords in Safari.[/footnote]

### 5. Understand how 1-time passwords work and why you need them

For every app that accesses your account, you’ll need a specific password that is different than your main password. Each service issues these passwords slightly differently, and when you first setup 2SV, you’re likely to get all kinds of error messages and dialogues that tell you your password is wrong in different apps–especially email-related apps.

So, for example, I have Fantastical set up to sync my Apple iCloud calendar. That means I need to login to my [Apple account](https://appleid.apple.com/) online, generate a 1-time password for Fantastical, and paste that into the app. Don’t worry about saving these passwords–they are useless once you put enter them in the app and are only used once.

You’ll have to do this with all of your apps that use your accounts, so that can take some extra time on the front end. Again, it’s worth it. I also save the page where I can access the single-use passwords into 1Password, so I can just click it and quickly get a password. Here are the pages to generate passwords for the services I use. [footnote]I don’t have Evernote or Dropbox listed, because they don’t generate app-specific passwords but instead just “link” your account once you’re logged in. That’s a more elegant way to do things, but not really possible for Google or Apple because of how email clients work, as far as I can tell.[/footnote]

[Apple's site for app-specific passwords](https://appleid.apple.com/account/manage/security)

[Google's site for app-specific passwords](https://security.google.com/settings/security/apppasswords)

### 6. Get your terminology straightened out

I’ve been tossing the word code around here like candy, and there are a few different distinct codes, so I want to clarifying them a bit further.

  * Your **password**–that would be exactly how you think of your password currently–the main thing you use to access websites, apps, and services
  * Your **generated login code**–that’s the 4- to 6-digit numerical code you need every time you login to a service or app from a new device
  * Your **recovery code**–that’s the _I-truly-can’t-tell-you-how-stinking-important-this-thing-is code_ that is your spare-key-under-the-mat for getting into services if you lose your device. You’ll hopefully _never_ have to use this thing, but you’ll need to keep it safe, and in a few different places, to make sure you have it if you lose your verification device (i.e. your phone).

## More Good Stuff about 2SV

### If something gets stolen, you can remotely disable services

Of course, there’s the option to just permanently wipe your device if you’re using Apple products, but not all smartphones have the “kill switch” enabled. So, if you want to be able to nix access to key accounts: email, Dropbox, Evernote, 2SV is for you.

To do this, you’ll just need to login to the service you want to shut down remotely. Navigate to your history of generated passwords and click &#8220;Revoke Access&#8221; to that app on that device. Boom!

### If your password is compromised, you’re still ok

If your password is stolen, a bad guy still needs to have a secondary device. Of course, it’s a good idea to change your password once you know this, but the extra security should help you sleep better at night.

## The Links You Need

[Twofactorauth.org](https://twofactorauth.org) has a list of tons of services and information about each and 2SV.

### Apple

If you use iCloud with any third party apps, such as email, address book, or calendar clients, you can create app-specific passwords that let you sign in securely, even if the app that you’re using doesn’t support two-step verification.

Via [Apple’s site](http://support.apple.com/en-us/HT204152) on 2SV.

> Generate an app-specific password:
> 
>   1. Go to [My Apple ID](https://appleid.apple.com/).
>   2. Select Manage your Apple ID and sign in.
>   3. Select Password and Security.
>   4. Click Generate an App-Specific Password.

### Dropbox

Here’s Dropbox’s [blog post](https://blog.dropbox.com/2014/10/have-you-enabled-two-step-verification/) about 2SV.

Click here to enable [2SV with Dropbox](https://www.dropbox.com/account#security). Just click Enable under two-step verification.

### Evernote

Here’s Evernote’s [blog post](https://blog.evernote.com/blog/2013/10/04/two-step-verification-available-to-all-users/) about 2SV.

Click here to enable [2SV with Evernote](https://www.evernote.com/secure/SecuritySettings.action).

### Google

Here’s Google’s main page and pitch for getting you started with 2SV. Just scroll to the bottom and click get started.

Click here to enable [2SV with Google](https://www.google.com/landing/2step/)

Page to generate an [app-specific password](https://security.google.com/settings/security/apppasswords) with Google.

### 1Password

I _promise_ 1Password didn’t pay me to write this post. I can’t help but evangelize about it. Here you can pick up a copy of [1Password for your Mac](https://itunes.apple.com/us/app/1password-password-manager/id443987910?mt=12&at=11l4uNett) ($50), and here is [1Password for iOS](https://itunes.apple.com/us/app/1password-password-manager/id568903335?mt=8) (Free with a $10 in-app purchase).

## (Finally) Wrapping Up

Hopefully this process wasn't too painful or confusing. As I prefaced, I think this is an unfortunate but necessary step we need to take to get our lives locked down online. If there's anything that's unclear, I'd love to help and clarify so you can keep the services and accounts you use and love completely to yourself.
