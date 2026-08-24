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

## Table of contents

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [kubectl_arch](#kubectl_arch)
  - [minio_access_key](#minio_access_key)
  - [minio_client_arch](#minio_client_arch)
  - [minio_client_url](#minio_client_url)
  - [minio_cpu_shares](#minio_cpu_shares)
  - [minio_cronjobs](#minio_cronjobs)
  - [minio_default_labels](#minio_default_labels)
  - [minio_default_publish](#minio_default_publish)
  - [minio_default_volumes](#minio_default_volumes)
  - [minio_domain](#minio_domain)
  - [minio_extra_labels](#minio_extra_labels)
  - [minio_extra_publish](#minio_extra_publish)
  - [minio_extra_volumes](#minio_extra_volumes)
  - [minio_group](#minio_group)
  - [minio_image](#minio_image)
  - [minio_memory_limit](#minio_memory_limit)
  - [minio_memory_soft_limit](#minio_memory_soft_limit)
  - [minio_memory_swap](#minio_memory_swap)
  - [minio_network](#minio_network)
  - [minio_number_of_cpus](#minio_number_of_cpus)
  - [minio_prometheus_auth_type](#minio_prometheus_auth_type)
  - [minio_pull_image](#minio_pull_image)
  - [minio_region](#minio_region)
  - [minio_secret_key](#minio_secret_key)
  - [minio_user](#minio_user)
  - [minio_volume_server](#minio_volume_server)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

## Default Variables

### kubectl_arch

Architecture for the kubectl release

### minio_access_key

For security reasons you should overwrite this value by your own

#### Default value

```YAML
minio_access_key: 69c353dfb7d5caa1a0f8eaf91f52120dc7f713c9
```

### minio_client_arch

#### Default value

```YAML
minio_client_arch: "{{ 'arm64' if ansible_facts['architecture'] in ['aarch64', 'arm64'] else 'amd64' }}"
```

### minio_client_url

Download URL for Minio CLI

#### Default value

```YAML
minio_client_url: https://dl.minio.io/client/mc/release/linux-{{ minio_client_arch }}/mc
```

### minio_cpu_shares

CPU shares with Docker deployment

#### Default value

```YAML
minio_cpu_shares:
```

#### Example usage

```YAML
minio_cpu_shares: '512'
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

### minio_default_labels

List of default labels to assign to docker

#### Default value

```YAML
minio_default_labels: []
```

### minio_default_publish

List of default port publishing for docker

#### Default value

```YAML
minio_default_publish: []
```

#### Example usage

```YAML
minio_default_publish:
  - 127.0.0.1:9000:9000
```

### minio_default_volumes

List of default volumes to mount for docker

#### Default value

```YAML
minio_default_volumes:
  - '{{ minio_volume_server }}:/var/lib/minio'
```

### minio_domain

Domains to access this instance

#### Default value

```YAML
minio_domain: localhost
```

### minio_extra_labels

List of extra labels to assign to docker

#### Default value

```YAML
minio_extra_labels: []
```

### minio_extra_publish

List of extra port publishing for docker

#### Default value

```YAML
minio_extra_publish: []
```

#### Example usage

```YAML
minio_extra_publish:
  - 127.0.0.1:9000:9000
```

### minio_extra_volumes

List of extra volumes to mount for docker

#### Default value

```YAML
minio_extra_volumes: []
```

#### Example usage

```YAML
minio_extra_volumes:
  - /path/to/host/folder1:/path/within/container1
  - /path/to/host/folder2:/path/within/container2
  - /path/to/host/folder3:/path/within/container3
```

### minio_group

System group for the Minio service

#### Default value

```YAML
minio_group: minio
```

### minio_image

Docker image to use

#### Default value

```YAML
minio_image: webhippie/minio:latest
```

### minio_memory_limit

Memory limit with Docker deployment

#### Default value

```YAML
minio_memory_limit:
```

#### Example usage

```YAML
minio_memory_limit: 1024m
```

### minio_memory_soft_limit

Soft memory limit with Docker deployment

#### Default value

```YAML
minio_memory_soft_limit:
```

#### Example usage

```YAML
minio_memory_soft_limit: 512m
```

### minio_memory_swap

Swap usage with Docker deployment

#### Default value

```YAML
minio_memory_swap:
```

#### Example usage

```YAML
minio_memory_swap: 2048m
```

### minio_network

Optional docker network to attach

#### Default value

```YAML
minio_network:
```

### minio_number_of_cpus

Number of CPUs with Docker deployment

#### Default value

```YAML
minio_number_of_cpus:
```

#### Example usage

```YAML
minio_number_of_cpus: '1.0'
```

### minio_prometheus_auth_type

Auth type for prometheus endpoint

#### Default value

```YAML
minio_prometheus_auth_type: public
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

### minio_user

System user for the Minio service

#### Default value

```YAML
minio_user: minio
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
