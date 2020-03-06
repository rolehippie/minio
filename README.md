# minio

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/minio/status.svg)](https://cloud.drone.io/rolehippie/minio)

Ansible role to configure minio

## Table of content

* [Default Variables](#default-variables)
  * [minio_access_key](#minio_access_key)
  * [minio_cert_resolver](#minio_cert_resolver)
  * [minio_client_url](#minio_client_url)
  * [minio_cronjobs](#minio_cronjobs)
  * [minio_domains](#minio_domains)
  * [minio_image](#minio_image)
  * [minio_insecure_middlewares](#minio_insecure_middlewares)
  * [minio_network](#minio_network)
  * [minio_prefixes](#minio_prefixes)
  * [minio_prometheus_auth_type](#minio_prometheus_auth_type)
  * [minio_publish_server](#minio_publish_server)
  * [minio_region](#minio_region)
  * [minio_secret_key](#minio_secret_key)
  * [minio_secure_middlewares](#minio_secure_middlewares)
  * [minio_volume_server](#minio_volume_server)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### minio_access_key

For security reasons you should overwrite this value by your own

#### Default value

```YAML
minio_access_key: 69c353dfb7d5caa1a0f8eaf91f52120dc7f713c9
```

### minio_cert_resolver

Cert resolver within traefik

#### Default value

```YAML
minio_cert_resolver: default
```

### minio_client_url

Download URL for Minio CLI

#### Default value

```YAML
minio_client_url: https://dl.minio.io/client/mc/release/linux-amd64/mc
```

### minio_cronjobs

List of cronjob definitions for maintenance

#### Default value

```YAML
minio_cronjobs: []
```

#### Example usage

```YAML
minio_cronjobs:
  - name: maintenance
    minute: '0'
    hour: '0'
    day: '*'
    month: '*'
    weekday: '*'
    job: mc rm --older-than 30d --recursive --force bucket/logs
```

### minio_domains

Domains to access this instance

#### Default value

```YAML
minio_domains:
  - localhost
```

### minio_image

Docker image to use

#### Default value

```YAML
minio_image: webhippie/minio:latest
```

### minio_insecure_middlewares

Insecure middlewares for traefik

#### Default value

```YAML
minio_insecure_middlewares:
  - https@file
  - errors@file
```

### minio_network

Docker network to connect to

#### Default value

```YAML
minio_network: traefik
```

### minio_prefixes

Optional path prefixes to access it

#### Default value

```YAML
minio_prefixes: []
```

### minio_prometheus_auth_type

Auth type for prometheus endpoint

#### Default value

```YAML
minio_prometheus_auth_type: public
```

### minio_publish_server

Publish the service on that binding

#### Default value

```YAML
minio_publish_server:
```

### minio_region

Region used within this instance

#### Default value

```YAML
minio_region: us-east-1
```

### minio_secret_key

For security reasons you should overwrite this value by your own

#### Default value

```YAML
minio_secret_key: 954cde1f5a3c9b090584e7794ab9a71f9d11d7a1
```

### minio_secure_middlewares

Secure middlewares for traefik

#### Default value

```YAML
minio_secure_middlewares:
  - secure@file
  - errors@file
```

### minio_volume_server

Path to server volume

#### Default value

```YAML
minio_volume_server: /var/lib/minio
```

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
