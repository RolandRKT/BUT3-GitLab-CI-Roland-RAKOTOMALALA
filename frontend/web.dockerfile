# frontend/web.dockerfile

# Étape 1 : Build du front
FROM node:latest AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build   # construit dans /app/dist

# Étape 2 : Image finale avec serveur statique
FROM ghcr.io/static-web-server/static-web-server:2
COPY --from=build /app/dist /public
