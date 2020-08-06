A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.


# Grubb Lab Information
This is information on how to update the website, last updated by Kate Spencer on 8/6/2020. In general to make changes, add this repo to your GitHub Desktop, edit the files, then commit and push to the master branch. Changes take a few minutes to update, so if nothing seems to be changes give it a minute. There is also an option to test locally, but I have never used it, and instead just flag in progress pages with "Page Under Construction (Todays Date)". 

## How to update GrubbLab
This is the simplest page to update, it is simply a markdown file in the _pages folder. Images are stored in the images folder, and referenced useing HTML. The trickiest part is the format of bios and images, which are laid out using HTML `<divs>` but should be evident based on the existing format. 

## How to update publications
The publications page is made up of several files, first publications.md in _pages that controls the main/landing page with the list of publications with links. Then there is pubsFromBib.py in markdown_generator which generates the pages for the individual posts from book.bib, journal.bib, and pubs.bib. Finally, there is the _publications folder that contains markdown files for each publication. 

The individual markdown files are generated when pubsFromBib.py is run(I just use IDLE but any python IDE should work fine). This is a little tricky to run the first time, as there are a few dependancies but after is very simple. To run pubsFromBib.py up we need pybtex, which can be installed from [pip](https://pip.pypa.io/en/stable/installing/). Pip comes installed with any of the recent python updates, I had to [set the PATH in myenvironment variables](https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command) in order to make it work. Once your pip is working, you can simply enter `pip install pybtex` into your terminal to install [pybtex](https://pybtex.org/). Once pubsFromBib.py runs without error, any time you run it, it will automatically update every file in _publications based on the information in the .bib files, and create files for any publication without one. To update the information in the markdown pages, you must first update the .bib files from markdown_generator. To do this, I simply open them in Zoterro, edit them, then save them back into markdown_generator with the same names and overwrite the old versions(make sure to save the notes also!). There are some subtle - but important - distinctions between pubs.bib, journal.bib and book.bib, and they are made based on how pubsFromBib.py reads the venuekey. It is a little bit of a pain, and probably could/should be improved, but for now, any journals go in journal.bib, Alicia's PHD Thesis goes in book.bib and everything else (conference and workshop papers) go in pubs.bib to prevent any errors. Links to the Author PrePrint, Supplimental Information, and Talk Slides are written in markdown in a "note" in Zoterro, and when the markdown page is built by pubsFromBib.py it is included simply as markdown and can be read into the page. Some links are already hosted on [Dr. Grubb's Toronto site](http://www.cs.toronto.edu/~amgrubb/), but local PDF's are in the files folder.

Once pubsFromBib.py is run, all the pages are generated and there is nothing more needed! If you wish to add additional infromation it is important to do it in the appropriate .bib file, or else that information is overwritten each time pubsFromBib.py is run. The only exception to this is the dagger(†) symbol used to indicate a Toronto author(Gary Song and Caroline Hu). This symbol is not recognized by pybtex, and instead is conferted into a diamond with a question mark which will not allow the site to build, and you will get an email with an error message.  
### Make sure that there are no unknown symbols (diamond with question mark) in any files or the website will not build. These will be automatically generated when pubsFromBib.py is run, but should be replaced with daggers (†) prior to commiting the changes.

## How to update Projects
Projects is based on the "blog post" framework from Academic Pages, and is fairly similar to Publications, except content is not automatically generated. The projects.html file in the _pages folder controls the layout on the main page, then _posts has the markdown files with the text of each individual post. Because the projects page is based on a blog post format, you MUST include a full date in YYYY-MM-DD format, though it is not published anywhere. To make a new post, simply duplicate an old one, and rename it, ensuring that the `permalink` matches the name of the file. 

## Notes on layout
Due to some changes to the exerpts displayed on the main pages of projects and publication as well as making projects less like a blog, the code for the layouts is a little funky. The main pages for projects and publications use archive-project.html(found under _includes), and about and individual projects(posts) and publications use archive.html(in _layouts). There was an issue where the footer had no format and was in a weird place, so archive.html fixes this by forcing it in, which isn't the cleanest. Archive-project.html was created to distinguish between publications and projects, but eventually was used for both. When simply adding information, the layouts shouldn't be an issue but I wanted to include a bit of information which hopefully will make it easier if they ever do need to be changed.


# Origional Information from Academic Pages Author
I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
