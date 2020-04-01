# Screening Scheduler

Goal of this project is to create a simple workflow so that interviewers can give candidates slots of available time when they can have a screening interview.

## Technical goals
1. Learn python using Flask
2. Keep it simple, idea is to provide url link to candidate.
3. Create unit test.
4. Use new framework to build admin SPA

## Workflow admin
Admin tool can be a SPA (use new framework)
1. Interviewer creates personal calendar, by providing:
  * Full name
  * email
  * public name (this will be used in the final url)

2. Interviewer selects calendar, and creates a new candidate, by providing:
  * Candidate's name
  * Week of year when interviwer is available.
  * Add slots when interviewer is available, E.g Select Monday at 10am, Tuesday at 11am, etc..

3. Slots are displayed in calendar, so that they won't be available for next candidate creation
4. New url is provided so that you can send that url over the candidates, and they'll get to decide which slot works better for meeting/talking.


## Workflow candidate
1. Interviewer sends over url E.g https://mycompany.com/interviews/:interviewer's public name/c=${token}
2. Candidate clicks on link, and a calendar will be displayed with the available interviewer's slots
3. Candidate can click on any of this slots
4. Modal will be displayed after users clicks on a slot to provide following info:
  * Candidate full name
  * Candidate phone number

## Admin endpoints
POST /calendars
  Content-Type: application/json
  Body: {
    "interviewerFullName": "",
    "interviewerEmail": "",
    "calendarName": ""
  }

GET /calendars
