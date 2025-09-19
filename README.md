# Setup Subscription & Resource Group
- **Create a subcription plan**

![image](./assets/3.PNG)

- **Create Resource Group**

![image](./assets/37.PNG)

# Entra App Registrations

- **Register new app via `App Registrations`**

![image](./assets/1.PNG)
![image](./assets/2.PNG)

# Create API Secret key
- Go to `App Resgistrations` > `<Your App>` > `Certificates & secrets`

![image](./assets/4.PNG)

- **Record info below for later**
    - **App (Client) ID** as the Bot ID in Teams manifest.
    - **Client secret** for bot authentication or Graph API calls.

![image](./assets/5.PNG)
![image](./assets/6.PNG)

# Create Azure Bot
- **Go to `All Resources` > `AI Apps and Agents` > `Azure Bot`**

![image](./assets/7.PNG)
![image](./assets/8.PNG)

- **Use `App ID` and `Tenant ID` from `App Registrations`**

![image](./assets/9.PNG)

- **Configure messaging endpoint**

![image](./assets/10.PNG)

- **Add MS Teams as Channel**

![image](./assets/11.PNG)

# Create Work-Email User (Global admin)

- **Go to `Entra ID` > `Users`**

![image](./assets/29.PNG)
![image](./assets/30.PNG)
![image](./assets/31.PNG)

# Microsoft 365 Business Premium License
- **Access to https://admin.microsoft.com**
- **Purchase Microsoft 365 Business Premium License via 1-Month trial**

![image](./assets/32.PNG)

- **Grant license to user**

![image](./assets/33.PNG)
![image](./assets/34.PNG)

# Create MS Teams App

- **Go to https://dev.teams.microsoft.com/**
- **Login using EntraID user email**

![image](./assets/20.PNG)

- **Create new app**

![image](./assets/21.PNG)
![image](./assets/22.PNG)

- **Refer to `Azure` > `App Registrations` > `<YOUR_APP>` > `Client ID` for The Client ID below**

![image](./assets/23.PNG)

- **Create Bot in `App features`**

![image](./assets/24.PNG)

- **Refer to `Azure` > `App Registrations` > `<YOUR_APP>` > `Client ID` for The Bot ID below**

![image](./assets/25.PNG)

- **Set Permissions**

![image](./assets/26.PNG)

- **Publish app**

![image](./assets/27.PNG)
![image](./assets/28.PNG)

# Admin App Approval
- **Access to https://admin.teams.microsoft.com**
- **Must use Global Admin user to login and approve**

![image](./assets/35.PNG)

# Install MS Teams App
- **Login MS Teams App to install**

![image](./assets/36.PNG)
![image](./assets/38.PNG)

# Messaging Endpoint
- **Start up this docker container** via `docker compose up -d`
- **Expose to public network via** `ssh -R 80:localhost:5000 serveo.net`

![image](./assets/40.PNG)

- **Update Messaging Endpoint in `Azure Bot`**

![image](./assets/39.PNG)



