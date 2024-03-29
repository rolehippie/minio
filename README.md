# minio

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/minio)
[![General Workflow](https://github.com/rolehippie/minio/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/minio/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/minio/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/minio/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/minio/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/minio/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/minio)](https://github.com/rolehippie/minio/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.minio-blue)](https://galaxy.ansible.com/rolehippie/minio)

Ansible role to install and configure MinIO.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [minio_access_key](#minio_access_key)
  - [minio_cert_resolver](#minio_cert_resolver)
  - [minio_client_url](#minio_client_url)
  - [minio_cronjobs](#minio_cronjobs)
  - [minio_domains](#minio_domains)
  - [minio_image](#minio_image)
  - [minio_insecure_middlewares](#minio_insecure_middlewares)
  - [minio_network](#minio_network)
  - [minio_prefixes](#minio_prefixes)
  - [minio_prometheus_auth_type](#minio_prometheus_auth_type)
  - [minio_publish_server](#minio_publish_server)
  - [minio_pull_image](#minio_pull_image)
  - [minio_region](#minio_region)
  - [minio_secret_key](#minio_secret_key)
  - [minio_secure_middlewares](#minio_secure_middlewares)
  - [minio_volume_server](#minio_volume_server)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

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
minio_cert_resolver:
```

#### Example usage

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
minio_network:
```

#### Example usage

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

### minio_pull_image

Pull image as part of the tasks

#### Default value

```YAML
minio_pull_image: true
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

## Discovered Tags

**_minio_**


## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)
- [community.docker](https://github.com/ansible-collections/community.docker)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
