import datetime
import typing

import kubernetes.client

class V1Volume:
    aws_elastic_block_store: typing.Optional[
        kubernetes.client.V1AWSElasticBlockStoreVolumeSource
    ]
    azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource]
    azure_file: typing.Optional[kubernetes.client.V1AzureFileVolumeSource]
    cephfs: typing.Optional[kubernetes.client.V1CephFSVolumeSource]
    cinder: typing.Optional[kubernetes.client.V1CinderVolumeSource]
    config_map: typing.Optional[kubernetes.client.V1ConfigMapVolumeSource]
    csi: typing.Optional[kubernetes.client.V1CSIVolumeSource]
    downward_api: typing.Optional[kubernetes.client.V1DownwardAPIVolumeSource]
    empty_dir: typing.Optional[kubernetes.client.V1EmptyDirVolumeSource]
    fc: typing.Optional[kubernetes.client.V1FCVolumeSource]
    flex_volume: typing.Optional[kubernetes.client.V1FlexVolumeSource]
    flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource]
    gce_persistent_disk: typing.Optional[
        kubernetes.client.V1GCEPersistentDiskVolumeSource
    ]
    git_repo: typing.Optional[kubernetes.client.V1GitRepoVolumeSource]
    glusterfs: typing.Optional[kubernetes.client.V1GlusterfsVolumeSource]
    host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource]
    iscsi: typing.Optional[kubernetes.client.V1ISCSIVolumeSource]
    name: str
    nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource]
    persistent_volume_claim: typing.Optional[
        kubernetes.client.V1PersistentVolumeClaimVolumeSource
    ]
    photon_persistent_disk: typing.Optional[
        kubernetes.client.V1PhotonPersistentDiskVolumeSource
    ]
    portworx_volume: typing.Optional[kubernetes.client.V1PortworxVolumeSource]
    projected: typing.Optional[kubernetes.client.V1ProjectedVolumeSource]
    quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource]
    rbd: typing.Optional[kubernetes.client.V1RBDVolumeSource]
    scale_io: typing.Optional[kubernetes.client.V1ScaleIOVolumeSource]
    secret: typing.Optional[kubernetes.client.V1SecretVolumeSource]
    storageos: typing.Optional[kubernetes.client.V1StorageOSVolumeSource]
    vsphere_volume: typing.Optional[kubernetes.client.V1VsphereVirtualDiskVolumeSource]
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[
            kubernetes.client.V1AWSElasticBlockStoreVolumeSource
        ] = ...,
        azure_disk: typing.Optional[kubernetes.client.V1AzureDiskVolumeSource] = ...,
        azure_file: typing.Optional[kubernetes.client.V1AzureFileVolumeSource] = ...,
        cephfs: typing.Optional[kubernetes.client.V1CephFSVolumeSource] = ...,
        cinder: typing.Optional[kubernetes.client.V1CinderVolumeSource] = ...,
        config_map: typing.Optional[kubernetes.client.V1ConfigMapVolumeSource] = ...,
        csi: typing.Optional[kubernetes.client.V1CSIVolumeSource] = ...,
        downward_api: typing.Optional[
            kubernetes.client.V1DownwardAPIVolumeSource
        ] = ...,
        empty_dir: typing.Optional[kubernetes.client.V1EmptyDirVolumeSource] = ...,
        fc: typing.Optional[kubernetes.client.V1FCVolumeSource] = ...,
        flex_volume: typing.Optional[kubernetes.client.V1FlexVolumeSource] = ...,
        flocker: typing.Optional[kubernetes.client.V1FlockerVolumeSource] = ...,
        gce_persistent_disk: typing.Optional[
            kubernetes.client.V1GCEPersistentDiskVolumeSource
        ] = ...,
        git_repo: typing.Optional[kubernetes.client.V1GitRepoVolumeSource] = ...,
        glusterfs: typing.Optional[kubernetes.client.V1GlusterfsVolumeSource] = ...,
        host_path: typing.Optional[kubernetes.client.V1HostPathVolumeSource] = ...,
        iscsi: typing.Optional[kubernetes.client.V1ISCSIVolumeSource] = ...,
        name: str,
        nfs: typing.Optional[kubernetes.client.V1NFSVolumeSource] = ...,
        persistent_volume_claim: typing.Optional[
            kubernetes.client.V1PersistentVolumeClaimVolumeSource
        ] = ...,
        photon_persistent_disk: typing.Optional[
            kubernetes.client.V1PhotonPersistentDiskVolumeSource
        ] = ...,
        portworx_volume: typing.Optional[
            kubernetes.client.V1PortworxVolumeSource
        ] = ...,
        projected: typing.Optional[kubernetes.client.V1ProjectedVolumeSource] = ...,
        quobyte: typing.Optional[kubernetes.client.V1QuobyteVolumeSource] = ...,
        rbd: typing.Optional[kubernetes.client.V1RBDVolumeSource] = ...,
        scale_io: typing.Optional[kubernetes.client.V1ScaleIOVolumeSource] = ...,
        secret: typing.Optional[kubernetes.client.V1SecretVolumeSource] = ...,
        storageos: typing.Optional[kubernetes.client.V1StorageOSVolumeSource] = ...,
        vsphere_volume: typing.Optional[
            kubernetes.client.V1VsphereVirtualDiskVolumeSource
        ] = ...
    ) -> None: ...
