# Cloud Lab 10 Submission: CloudFormation and Terraform

| | |
| --- | --- |
| **Student name** | Rin Nairith |
| **Student ID** | e20221557 |
| **Learner Lab user name** | voclabs/user5623079=RIN_NAIRITH |
| **CloudFormation stack** | `cf-lab-stack` |
| **Terraform status** | Blocked by SCP `p-m1m8ob9n` |
| **Date completed (Part 10.1)** | 2026-10-31 |
| **Region** | US East (N. Virginia) `us-east-1` |

> Part 10.1 complete. Part 10.2 blocked.

---

## Part 10.1 — CloudFormation

![Initial stack resources](images/01-cf-resources.png)

`cf-lab-stack` created a `t2.micro` instance and a security group allowing HTTP `80` and SSH `22`.

![Initial stack outputs](images/02-cf-outputs.png)

`InstanceEndpoint`: `http://ec2-54-227-105-101.compute-1.amazonaws.com:80`

![First browser test](images/03-cf-browser.png)

**Hello World from Educative**

### Updated stack

![Updated stack resources](images/04-cf-updated-resources.png)

Added `SecondInstance` and `SecondSecurityGroup`. Stack status: `UPDATE_COMPLETE`.

![Updated stack outputs](images/05-cf-updated-outputs.png)

| Output | Endpoint |
| --- | --- |
| `InstanceEndpoint` | `http://ec2-3-93-194-198.compute-1.amazonaws.com:80` |
| `SecondInstanceEndpoint` | `http://ec2-54-83-117-138.compute-1.amazonaws.com:80` |

![Second browser test](images/06-cf-second-browser.png)

**Hello World from Second Instance**

## Part 10.2 — Terraform (blocked)

The S3 bucket `cc-gic-e20221557-lab10-site-20261031` was created, but Terraform fails while refreshing it.

- `s3:GetBucketObjectLockConfiguration` → `403 AccessDenied`
- Denied by AWS Organizations SCP `p-m1m8ob9n`
- AWS provider `4.67.0` and `5.100.0` both fail; changing versions did not help
- State contains only the S3 bucket; Lambda and Function URL were not applied
- Screenshots `07`–`16` are not included or marked complete
