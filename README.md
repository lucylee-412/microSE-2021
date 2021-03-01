# microSE_2-26

###### Contributors: Lucy Lee, Kelia Morrah

Assignment: Take the given Midterm Project files from the first half of the group project, and revamp the site.

We decided to go with an anime theme, and assigned each member an HTML file.
- [Home page](https://lucylee-412.github.io/microSE_2-26/Home.html) (originally SiestaCon) - **Artem**
- [Anime character facts](https://lucylee-412.github.io/microSE_2-26/Bio.html) (originally state facts & postcard generator) - **Kelia**
- [Contact form & random button generator](https://lucylee-412.github.io/microSE_2-26/Contact.html) (originally Helping Hands contact form) - **Lucy**

### Change Log:
*3/1:*
- **Lucy**
  - On closer inspection, I do not believe the .txt files in the snippets folder are needed at all. They are never called on, and are merely a copy of the data set used in Bio.html and Home.html. The normalize1.css is never used either. However, I'll leave them there for now, because we may want to call upon them in the future.
  - Fixed indenting, and added additional comments that thoroughly reference which .css files were used in all HTML files.
  - Renamed Quiz.html as Contact.html to reflect my intention of adding a form back in.
  - All HTML files now have the same banners. Leaving the inconsistent footers alone for now.

*2/28:*
- **Lucy**
  - Added some comments to Bio.html, detailing which CSS files were used for each div classes.
  - Redid some of the code for outer-wrapper class and img-holder class to re-stylize font and resize images in Bio.html.
  - Replaced .png images that did not have a working transparent background. Need updated version of LAK logo from Kelia; in the meantime, will switch back to default SiestaCon banner.

*2/27:*
- **Lucy**
  - Debugged code in Bio.html (renamed; originally Postcards.html) to include missing curly braces, and matching variable + function names.
  - Removed the half with the postcard generator off the page.

*2/26:*
- **Kelia**
  - Created a character-data.js script to use as a database for the table generators in Postcards.html. Replaced all "state" data in the original Midterm Project file with "character" data.
- **Lucy**
  - Created a button on Quiz.html (renamed; originally VolunterApp.html) with form.css that uses characters.js to generate a random image. Currently not working as intended, but I will figure something out.
