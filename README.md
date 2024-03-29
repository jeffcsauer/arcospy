# arcospy

[![PyPI version](https://badge.fury.io/py/arcospy.svg)](https://badge.fury.io/py/arcospy)

## Introduction

Welcome to `arcospy`, the python version of the [R `arcos` package](https://github.com/wpinvestigative/arcos) maintained by *The Washington Post*. `arcospy` is the result of a R-to-python translation project carried out at the University of Maryland in the Fall of 2019. The project was motivated a *Washington Post* data-driven [story](https://www.washingtonpost.com/graphics/2019/investigations/dea-pain-pill-database/#download-resources) on a large pain pill database recently made publicly available.

The `arcospy` module was built to offer the exact same functionality as `arcos`, with the only difference being the ability to run the API calls in `python`! All of the commands in `arcospy` inherit the names from the original commands in `arcos`. Both `arcos` and `arcospy` act as wrappers for the [DEA ARCOS dataset](https://arcos-api.ext.nile.works/__swagger__/).

## Installation

`arcospy` is hosted on PyPI and is `pip` installable. To install `arcospy` on your machine, start a new terminal and run the following commands:

`$ pip install arcospy`

## Requirements

`arcospy` requires `pandas>=0.20.0` and `requests>=2.0.0`. You may need to manually install these requirements if the build does not trigger.

## Updates

**Updates (will be posted periodically)**:
- 1/22/2024: Fixed install issues.
- 11/25/2023: Updated main `url` where the Washington Post is storing the data. Reorganized repo for readability. All commands should be back up and running. 
- 5/20/2021: Changes in API payload required a minor update to certain raw data commands.
- 9/14/2020: Updated docs to reflect forthcoming publication of `arcos` and `arcospy` in *JOSS*.
- 8/1/2020: Renamed demos to docs for development consistency. Added another example notebook demonstrating acquisition and manipulation of pharmacy-level data. Planning gathering of additional ARCOS reports. 
- 3/18/2020: Added four new commands for business-level data, as well as updating documentation to reflect additional years now present in the data (up to 2014).
- 3/1/2020: Re-organized repository for readability. Updated testing documents. Fixed two small parameter issues with state-level query commands.  1.0.8 live and stable.
- 1/22/2020: Carried out PEP8 styling for commands, added help information, and package header. Re-published package as 1.0.6 as the package is now considered stable.  
- 1/14/2020: Reformatted `README.md` to provide more specific headers, installation instructions, requirements, and additional information.
- 12/10/2019: added a new folder called [demos](https://github.com/jeffcsauer/arcospy/tree/master/demos). Inculdes a basic getting started guide as well as an introduction to making the data spatial.

## Use

All functions are available on *The Washington Post* reference page [here](https://wpinvestigative.github.io/arcos/reference/index.html). Example notebooks in python are available in the [docs](https://github.com/jeffcsauer/arcospy/tree/master/docs) folder. Additional example use cases are available in R [here](https://wpinvestigative.github.io/arcos/articles/). 

Data can be gathered at the pharmacy, distributor, county, or state as the geographic unit of analysis. Depending on the geographic level, there may be raw, summarized, or supplemental data available. For example, the `county_raw()` command returns each individual ARCOS record for a given county from 2006 to 2014. However, the `summarized_county_annual()` command returns the annual summarized totals for a given county for each year of 2006 to 2014.

# Contributing

*[The following is lifted directly from `contributing.md`](https://github.com/jeffcsauer/arcos_arcospy_information/blob/master/contributing.md)*

Contributions are welcome to both `arcos` and `arcospy`. For major contributions, please fork the master `arcos` or `arcospy` branch and then open a pull request with the suggested changes. We will then review the change and determine if there is a generalizable solution to both `R` and `Python`. If there is no generalizable solution, we will still strive to make your contribution visible on the respective Github page.

## Documentation

Improvements to the documentation for `arcos` and `arcospy` are welcome. As stated above, we will try to generalize all contributions to both packages. For example, if the wording around a specific command is unclear, we can improve the wording in both packages. Additionally, if there are features of a command that you believe should be included in the primary documentation, please let us know so we can improve the user experience.

## Code

Presently, the core functionality of the API is maintained by the Data Reporting Team at *The Washington Post*. There is ample room for users to suggest functions that can be added to `arcos` and `arcospy`. For example, users might suggest functions that download national or regional sets of data by looping existing commands.

## Issues

Trackable issue pages are available on both the master `arcos` or `arcospy` Github pages. Issues may be related to anything from malfunctioning commands to inconsistent data. We encourage an active discussion and hope to readily address any errors. We recommend that when submitting an issue users provide specific tags and examples of the aberrant behavior. If you are able to solve an issue with the code independently, please open a pull request with the corrected code and a short explanation as to the bug fix.

---

**Disclaimer: please note that the author of this package, Jeff Sauer, is not affiliated with _The Washington Post_ in any official capacity.**
