---
title: 4 Tools to Make Language Learning Easier
author: Jordan Shirkman
type: post
date: 2014-11-20T10:00:37+00:00
url: /language-learning-tech/
categories:
  - Technology

---
I’m learning a second language for the second time. Normally you’d consider that a third language, but when you don’t properly learn a second language the first time (read: via high school Spanish), your second second language is really your first second language.

![Image](/static/images/macbook-air-iphone-moleskin.jpeg) 

After that clarification here are a couple tools I’ve been using to make language learning a bit more automatic on my Mac.

### 1. Using PopClip to make translation easier.

I’ve mentioned [my love of PopClip](https://jshirk.com/blog/daily-mac-apps/) before. It’s an extension that appears when you highlight text with your mouse on your Mac. There are two handy extensions you can find on the [PopClip](http://pilotmoon.com/popclip/) website. Translating via the [Google Translate](https://pilotmoon.com/popclip/extensions/page/GoogleTranslate) website and having a [pop-up translation](https://pilotmoon.com/popclip/extensions/page/InstantTranslate) appear.

For the latter, if I wanted to know what “Ne razumem” [footnote]Don’t worry, “ne razumem” is a phrase I’ve mastered in Slovene.[/footnote]means in Slovene, I can just highlight the text and click the PopClip extension that shows the translation overhead.

![Image](/static/images/PopClip-autotranslate.jpeg)![Image](/static/images/PopClip-autotranslate-2.jpeg) 

What’s special about the second extension with the popover is that the translation is displayed _and_ copied to your clipboard. I’ve found it better to translate from Slovene to English, thus setting English as the default option since I can guess what it means if the translation is a bit off. If I go the other direction, I’m likely to get a literal (i.e. bad) translation into Slovene.

Finally, I created an extension that searches the [PONS online dictionary](http://pons.com) in English and Slovene. You can customize for any languages PONS has, and it’s saved me a ton of copying and pasting and switching windows. I just highlight the word or phrase and click the extension and it brings up the website for me. You can download [PopMaker](http://brettterpstra.com/2014/05/12/popmaker-popclip-extension-generator/) to make your own extensions.

![Image](/static/images/PopMaker-example.jpeg) 

### 2. Using Drafts to keep track of new words

Another oft-praised app is [Drafts](https://jshirk.com/blog/drafts-ios/), and I use it to save new words I’m learning. I’ve found that when you’re learning a new language, you constantly have new vocabulary you hear but don’t understand. I type those words in a draft [footnote]with context, preferably[/footnote]and have an Evernote action set up to append those words to a running note. That means all the new words I’ve heard but haven’t figured out the meaning to are in the same list I can reference and research.

Here’s a screenshot of the action. I just use the default Evernote Drafts’ setting with the title of the note changed to my vocabulary list and change it from create to prepend, so my newest words are at the top.

![Image](/static/images/IMG_4704.jpeg) 

### 3. Using TextExpander for non-English characters

Slovene uses ?, š, and ž. I call them c, z, or s with a hat. [footnote]very technical language jargon[/footnote]Anyway, if you press and hold on a letter key when you’re on an iOS device or Mac, you have an option to choose a different variety of that letter.

That’s handy, but I never need the other versions of the letters when I’m typing, so it takes a few extra steps.

  1. Press and hold the letter
  2. Wait for the pop-up dialogue
  3. Choose the proper letter

On the Mac the system also creates different letters if you hold down the option button and press the letter.

![Image](/static/images/Letter-S-Pop-Up.jpeg) 

I never use the French c with a goatee (ç), the German little l 3 (ß) or Omega (?). So, I set TextExpander to automatically replace the Option + C or S or Z letters to replace with ?, š, and ž, or in the capital variety when I hold Shift + Option + C or S or Z.

To do that, just create a new snippet in TextExpander, place the character you want to type in your target language in the Content box and the default Option + Letter character in the Abbreviation box.

![Image](/static/images/TextExpander-letter-c.jpeg) 

### 4. Keyboard Maestro for searching words

I mentioned the PopClip option to search for words on the PONS dictionary. Unfortunately, not all websites are as good as PONS.

I use an older website called [Amebis](http://besana.amebis.si/pregibanje/) to look up conjugations of words in Slovene. I’m not sure how it works behind the scenes, but the website doesn’t return a new URL or search query, it just appears on the page.

So, I concocted a little KeyBoard Maestro expansion that copies a word, opens Safari, clears the text in the box, and pastes the copied word, and searches for the word. It saves me a ton of steps and hassle. It’s my favorite action I’ve created in Keyboard Maestro so far.

Here’s a 8-second video of how it works.



And here’s a screenshot of the workflow.

![Image](/static/images/Amebis-Workflow.jpeg) 

## What are your favorite tips for using technology to acquire new skills?
