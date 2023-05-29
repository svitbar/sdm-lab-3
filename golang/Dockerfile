FROM golang:1.20 AS builder 

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 go build -o build/fizzbuzz

FROM gcr.io/distroless/static

WORKDIR /build

COPY --from=builder /app/build/fizzbuzz ./fizzbuzz
COPY --from=builder /app/templates ./templates

CMD ["/build/fizzbuzz", "serve"]
