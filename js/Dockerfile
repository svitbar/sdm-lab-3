FROM node:16.20.0 as builder

WORKDIR /app

COPY package.json package-lock.json index.js ./

RUN npm ci

FROM astefanutti/scratch-node

COPY --from=builder /app /

ENTRYPOINT ["node", "index.js"]