# Testing - The Cookbook app

Return to main README file [README](https://github.com/asdub/laughing-cookbook/blob/master/README.md)

## Manual Testing 

#### Responsive Testing
Responsivity tested on physical iPhone & Anrdroid phones (iPhone 11 Pro Max / Samsung Galaxy s21)

Also tested within mobile device views in Chrome Dev Tools & Safari Web Tools.
The follow screen sizes were tested using both above tools: 

**iOS Mobile & Tablet devices**
| Device        | Pixel Size    | Viewport  |
| ------------- |:-------------:| ---------:|
|iPhone XR     | 828 x 1792.   | 414 x 896 |
|iPhone XS     | 1125 x 2436   | 375 x 812 |
|iPhone XS Max | 1242 x 2688   | 414 x 896 |
|iPhone X	    | 1125 x 2436	| 375 x 812 |
|iPhone 8 Plus  | 1080 x 1920	| 414 x 736 |
|iPhone 8	    | 750 x 1334	| 375 x 667 |
|iPhone 7 Plus	| 1080 x 1920	| 414 x 736 |
|iPhone 7	    | 750 x 1334	| 375 x 667 |
|iPhone 6/6S Plus|1080 x 1920   | 414 x 736 |
|iPhone 6/6S	|750 x 1334	    |375 x 667  |
|iPhone 5	    |640 x 1136	    |320 x 568  |		
|iPod Touch	    |640 x 1136	    |320 x 568  |	
|iPad Pro	    |2048 x 2732	|1024 x 1366|
|iPad 3 & 4 Gen	|1536 x 2048	|768 x 1024 |
|iPad Air 1 & 2	|1536 x 2048	|768 x 1024 |
|iPad Mini 2 & 3|1536 x 2048	|768 x 1024 |
|iPad Mini  	|768 x 1024	    |768 x 1024 |


**Anroid Mobile & Tablet devices**
| Device        | Pixel Size    | Viewport  |
| ------------- |:-------------:| ---------:|
|Nexus 6P	    | 1440 x 2560	|412 x 732q |
|Nexus 5X	    | 1080 x 1920	|412 x 732  |
|Google Pixel 4XL|1440 x 869	|412 x 869  |
|Google Pixel 4	| 1080 x 2280	|412 x 869  |
|Google Pixel 3a| 1080 x 2220	|412 x 846  |
|Google Pixel 3XL|1440 x 2960	|412 x 847  |
|Google Pixel 3	|1080 x 2160	|412 x 824  |
|Google Pixel 2	|1440 x 2560	|412 x 732  |
|Google Pixel XL|	1440 x 2560	|412 x 732  |
|Google Pixel	|1080 x 1920	|412 x 732  |

**Desktops & Browsers** *(Physical devices)*
| Device        | Browser    | Browser 2 | Browser 3 |
| ------------- |:----------:| ---------:| ---------:|
|MacBook Pro    | Chrome     | Safari    | Firefox    |
|Chromebook     | Chrome     | N/a       | N/a       |
|Dell (Win10)   | Chrome     | Edge      | Firefox.   | 
|Dell (Win7)	| IE11       | Firefox    | N/a       |

There were Less than ideal result on smaller mobile devices in landscape. 
But all elements are still visable and all features are usable. 
I did not tese on anything under IE11. 


### Manual testing process

    Header/ Navbar
    - Logo & navigation clearly visable and unobstructed.
    - When unauthorised, the following nav options should display:
        - Discover Recipes
        - Login
        - Register
    - Confirm authorised users see the following menu options:
        - Discover Recipes
        - Your Recipes 
        - Add Recipe
        - Logout
    - An admin user, in addition to the above should also see:
        - Admin Dashboard.
    - Confirm on medium/ small screens that the nav text changes to an icon and the sidebar is functional.
    - The sidebar, when active, should have the same menu options detailed above. 
    - Make sure the welcome text contains the correct recipe count. 
    - Confirm the 'Sign Up' CTA is only visable to unauthorised users. 
    - Conform the search functionality is working. Search items are: 
        - Recipe Title
        - Recipe Description
        - Recipe Ingredients 
        - Recipe Chef
    - Confirm the search reset button is working. 
    
    Main 
    - Confirm 20 recipe cards are visbale. 
    - Confrim there is no missing data from the cards, including:
        - Recipe Title
        - Recipe Description
        - Recipe Chef
        - Servings
        - Total Cook Time
    - Confirm the 'View Recipe' link is functioning.
    - Confirm cards are responsive and aligning to grid on small & medium screens. 

    Footer
    - Confirm footer is positioned correctly at the end of each page. 
    - All links are functioning. 
    


