<!-- Documentation start -->
<!-- Logo start -->
<img align="right" width="100" src="https://gcdnb.pbrd.co/images/nlDr0mgn0Nkp.png"></a>
<!-- Logo end -->
<a id="top"></a>
# DeliverEase [![GitHub release](https://img.shields.io/github/release/TeamCodeArena/DeliverEase.svg?style=flat-square)](https://github.com/TeamCodeArena/DeliverEase/releases)  [![License](https://img.shields.io/github/license/TeamCodeArena/DeliverEase.svg?style=flat-square)](https://opensource.org/licenses/MIT)  [![Slack](https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white)](https://join.slack.com/t/deliverease-group/shared_invite/zt-20af47vjo-msHq~8~PRsmi3x5~rMzs7g)
<img align="right" width="200" src="https://gcdnb.pbrd.co/images/UkjcafJdZxhy.png"></a>

### Empowering Delivery Partners, Connecting Communities
>DeliverEase is an innovative platform **designed to empower delivery partners** and foster **seamless connections between buyers and sellers** without the need for intermediaries. With a **user-friendly interface** and **efficient processes**, DeliverEase aims to **revolutionize the way goods are delivered**, making it convenient for both consumers and businesses.

## Table of Contents
- [Introduction](#introduction)
- [How it Works](#how-it-works)
  - [Order Placement](#order-placement)
  - [Post a Job](#post-a-job)
  - [Acceptance and Delivery](#acceptance-and-delivery)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Feedback](#feedback)
- [License](#license)
- [How you can reach us](#social-media)

[![Coverage](https://img.shields.io/codecov/c/github/TeamCodeArena/DeliverEase.svg?style=flat-square)](https://codecov.io/gh/TeamCodeArena/DeliverEase)  [![Issues](https://img.shields.io/github/issues/TeamCodeArena/DeliverEase.svg?style=flat-square)](https://github.com/TeamCodeArena/DeliverEase/issues)

## Introduction
DeliverEase is built on the foundation of **empowering delivery partners**, enabling them to earn income while providing **efficient delivery services** to the community. By **bridging the gap between buyers and sellers directly**, DeliverEase eliminates the need for intermediaries, leading to **faster deliveries** and **reduced costs**.

## How it Works ![Process](https://img.shields.io/badge/Process-Simplified-green?style=flat-square) ![Architecture](https://img.shields.io/badge/Architecture-MVC-lightgrey?style=flat-square) ![Deployment](https://img.shields.io/badge/Deployment-Heroku-purple?style=flat-square)

### Order Placement ![User Interaction](https://img.shields.io/badge/User%20Interaction-Smooth-blue?style=flat-square) ![Real-time](https://img.shields.io/badge/Real--time-Enabled-brightgreen?style=flat-square) ![Security](https://img.shields.io/badge/Security-SSL-yellow?style=flat-square)
1. **Click Order:** To place an order, Buyers can click on the **"Order Something" button** on the homepage, which will lead them to the **order details page**

2. **Enter Delivery Details:** On the order details page, the Buyer can specify the **delivery location**, **preferred delivery time**, and any **additional information** relevant to the delivery

3. **Pickup Information:** They can also **provide pickup details**, including the **location and time** when the delivery partner should collect the item for delivery

4. **Submit Order:** After providing all the necessary information, the Buyer can **submit the order request**

### Post a Job ![Post a Job](https://img.shields.io/badge/Post%20a%20Job-Enabled-blue?style=flat-square)
1. **Post a Job:** Sellers can post delivery jobs by **clicking on the "Post a Job" option on the homepage**

2. **Job Details:** They must **enter the job specifics**, including the **item to be delivered**, **pickup location**, **delivery location**, and **expected delivery time**

3. **Delivery Partner Assignment:** Once the job is posted, the nearest available delivery partner will have the option to accept the job **`(algorithms are still to be developed)`**

### Acceptance and Delivery ![Acceptance and Delivery](https://img.shields.io/badge/Acceptance%20and%20Delivery-Active-green?style=flat-square)
1. **Delivery Partner Selection:** The nearest available delivery partner can **view available jobs and accept** the ones that match their location and schedule

2. **Order Confirmation:** Once the delivery partner accepts the job the delivery process will begin

3. **Delivery Execution:** The delivery partner will **collect the item from the buyer's specified pickup location** and **deliver it to the buyer's specified delivery address**

4. **Confirmation from both sides:** You will get an **OTP at our website**, tell that to seller so that we can know that this order is completed

5. **Delivery Completion:** Once the delivery is successfully completed, both the buyer and seller will **receive notifications of the successful order**

## Key Features ![Platform](https://img.shields.io/badge/Platform-Web-brightgreen?style=flat-square) ![Language](https://img.shields.io/badge/Language-Python%2C%20HTML%2C%20CSS%2C%20Shell%2C%20JavaScript-blue?style=flat-square) ![Framework](https://img.shields.io/badge/Framework-Django-orange?style=flat-square) [![Innovation](https://img.shields.io/badge/Innovation-%F0%9F%9A%80-yellow?style=flat-square)](#key-features)
- Empowerment of delivery partners to **earn income on flexible schedules** [![Empowerment](https://img.shields.io/badge/Empowerment-%F0%9F%9A%80-brightgreen?style=flat-square)](#key-features)
- Direct **connection between buyers and sellers** without middlemen [![Seamless Connections](https://img.shields.io/badge/Seamless%20Connections-%F0%9F%94%97-blue?style=flat-square)](#key-features)
- Efficient and **seamless order placement process** [![Efficient Processes](https://img.shields.io/badge/Efficient%20Processes-%F0%9F%94%A5-orange?style=flat-square)](#key-features)
- Post a Job feature for buyers to **find suitable delivery partners**
- **Real-time job acceptance** [![Real-time Updates](https://img.shields.io/badge/Real--time%20Updates-%F0%9F%95%B0-brightgreen?style=flat-square)](#key-features)
- **Convenient pickup and drop-off services**
- **No tracking system** to ensure user privacy [![User Privacy](https://img.shields.io/badge/User%20Privacy-%F0%9F%94%90-blue?style=flat-square)](#key-features)

## Getting Started ![Getting Started](https://img.shields.io/badge/Getting%20Started-Ready-blueviolet?style=flat-square) [![Quick Setup](https://img.shields.io/badge/Quick%20Setup-6%20Steps-success?style=flat-square)](#quick-setup) [![Installation Guide](https://img.shields.io/badge/Installation%20Guide-Easy-brightgreen?style=flat-square)](#installation-guide)
To get started with DeliverEase using Django, follow these steps:
- **Clone the repository:** `git clone https://github.com/TeamCodeArena/DeliverEase`
- **Navigate to the project directory:** `cd DeliverEase`
- **Install the dependencies:** `pip install -r requirements.txt`
- **Make migrations with the command:** `python manage.py makemigrations`
- **Migrate the migrations made:** `python manage.py migrate`
- **Start the Django development server:** `python manage.py runserver`

Now, you should have the **DeliverEase Django application** up and running locally. You can access it by visiting **http://127.0.0.1:8000/** in your web browser. ![Yay!](https://img.shields.io/badge/Yay!-%F0%9F%8E%89%F0%9F%98%81-green?style=flat-square)

Please note that this is a **simplified installation guide** **assuming you have Django and Python already set up on your system.** If you encounter any issues during the installation process, make sure to check Django's official documentation or reach out for support. Happy delivering!

## Contributing [![Contributions Welcome](https://img.shields.io/badge/Contributions%20Welcome-%F0%9F%91%8D-green?style=flat-square)](#contributing)
<!-- TODO: Link Contribiute.md -->
We welcome contributions from the community to enhance DeliverEase. If you want to contribute, follow the steps in the [**`Contributing.md`**](Contributing.md) file.

## Feedback [![Feedback](https://img.shields.io/badge/Feedback-%F0%9F%92%AD-blue?style=flat-square)](#feedback)
We value feedback to improve our platform continuously. If you have any suggestions or encounter any issues, please [**open an issue**](https://github.com/TeamCodeArena/DeliverEase/issues).

## License [![License](https://img.shields.io/github/license/TeamCodeArena/DeliverEase.svg?style=flat-square)](https://opensource.org/licenses/MIT)
<!-- TODO: Link LICENSE.md -->
DeliverEase is released under the [**MIT License**](https://opensource.org/licenses/MIT). 
See [**`LICENSE.md`**](LICENSE) for more information.


## Social Media [![Join the Community](https://img.shields.io/badge/Join%20the%20Community-%F0%9F%92%AC-blueviolet?style=flat-square)](#contributing)
You can join our [![Slack](https://img.shields.io/badge/Slack-4A154B?style=flat&logo=slack&logoColor=white)](https://join.slack.com/t/deliverease-group/shared_invite/zt-20af47vjo-msHq~8~PRsmi3x5~rMzs7g) community.



<img align="right" width="100" src="https://gcdnb.pbrd.co/images/GbLnj1MXCQRu.jpg?o=1"></a>

---

Thank you for choosing DeliverEase! We hope this platform enhances your delivery experience and connects communities in a meaningful way. Happy delivering!

<div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
  <a href="#top" style="text-decoration: none; background-color: #007BFF; color: white; display: inline-flex; align-items: center; justify-content: center; padding: 10px 20px; border-radius: 50%;">
    <img src="https://img.icons8.com/ios/50/FFFFFF/circled-chevron-up.png" alt="Back to Top" style="width: 24px; height: 24px;">
    <span style="margin-top: 8px;">Back to Top</span>
  </a>
</div>
<!-- Documentation end -->
