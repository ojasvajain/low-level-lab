_## Problem Statement
Template based notification Service - Different users can save their templates in the system and later they will just send the variables in the template. Using those variables and template you need to send notification.

https://leetcode.com/discuss/post/6825950/kotak-sde3-interview-by-anonymous_user-m3w5/



## Notes
1. Entities - Template
2. Methods in Service
   - add_template(template obj)
   - str = render_template(id, variables)
   - send_notification(str)

Validation
1. Template should not contain {{ and }}
2. All variables should be defined and non-null, non-empty
3. 