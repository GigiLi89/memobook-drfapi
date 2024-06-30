Link to the frontend GitHub repository: [Frontend repo](https://github.com/GigiLi89/memobook)
Link to deployed Heroku app: [Heroku app](https://memobook-af0ef88c7472.herokuapp.com/)

Please find the README.md file in a seperate document here: [README.md](README.md)

---

# Testing

Throughout the development of the API, multiple manual testings were made to verify the functionality of the features. Below is the final manual testing of everything before submission:

## Manual Testing

| Testing endpoints |      |
| ----------------- | ---- |
| chats             | Pass |
| chats/:id/        | Pass |
| comments          | Pass |
| comments/:id/     | Pass |
| posts             | Pass |
| posts/:id/        | Pass |
| followers         | Pass |
| followers/:id/    | Pass |
| likes             | Pass |
| likes/:id/        | Pass |
| profiles          | Pass |
| profiles/:id/     | Pass |

Fun story: When testing the test above I recieved a 403 error. I tried for almost an hour to fix it, checked all the code and could not understand why it was saying 403 until I finally realized that I wasn't even logged in.. :P Apart from that, no errors and at least I know that works haha!

| Testing CRUD Functionality |                               |                 |                       |           |
| -------------------------- | ----------------------------- | --------------- | --------------------- | --------- |
| App                        | Action                        | Authenticated   | Not authenticated     | Pass/Fail |
| Chats                      | See chats list                | 200 Ok          |                       |           |
| Chats                      | Create chat with another user | 201 Created     | 403 Not authenticated | Pass      |
| Chats                      | Create chat with yourself     | 400 Bad request | No available          | Pass      |
| Chats                      | Delete chat                   | 204 No content  | No available          | Pass      |
| Comments                   | See comments list             | 200 Ok          | 200 Ok                | Pass      |
| Comments                   | Create comment                | 201 Created     | No available          | Pass      |
| Comments                   | Edit comment                  | 200 Ok          | No available          | Pass      |
| Comments                   | Delete comment/:id            | 204 No content  | No available          | Pass      |
| Posts                      | See posts list                | 200 Ok          | 200 Ok                | Pass      |
| Posts                      | Create post                   | 201 Created     | No available          | Pass      |
| Posts                      | Edit post                     | 200 Ok          | No available          | Pass      |
| Posts                      | Delete post                   | 204 No conent   | No available          | Pass      |
| Followers                  | Show followers list           | 200 Ok          | 200 Ok                | Pass      |
| Followers                  | Follow another user           | 201 Created     | No available          | Pass      |
| Followers                  | Follow an existing follow     | 400 Bad request | No available          | Pass      |
| Followers                  | Delete a follow               | 204 No content  | No available          | Pass      |
| Likes                      | Show likes list               | 200 Ok          | 200 Ok                | Pass      |
| Likes                      | Like a post                   | 201 Created     | No available          | Pass      |
| Likes                      | Like an already existing like | 400 Bad request | No available          | Pass      |
| Likes                      | Delete like                   | 204 No content  | No available          | Pass      |
| Profiles                   | Show profiles list            | 200 Ok          | 200 Ok                | Pass      |
| Profiles                   | Show specific profile by id   | 200 Ok          | 200 Ok                | Pass      |

## Validating Code with CI Python Linter (https://pep8ci.herokuapp.com/)

No major issues, only a few missing blanks at the end which is resolved now. 

![CI Linter](assets_md/ci_linter_m.png)

---

Please find the README.md file in a seperate document here: [README.md](README.md)