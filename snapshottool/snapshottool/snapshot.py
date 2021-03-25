import boto3
def create_instance_snapshot(tags):
    ec2 = boto3.resource('ec2')
    if not tags:
        return print("No tags were provided")
    else:
        print ("The script will backup instances with tags:")
        for i in tags:
            print(f"Name: {i}, Value:{tags[i]}")
        for i in tags:
            for instance in ec2.instances.filter(
                Filters=[{
                    'Name': f"tag:{i}",
                    'Values': [f"{tags[i]}"]
                }]
            ):
                for device in instance.block_device_mappings:
                    ec2.create_snapshot(VolumeId=device.get('Ebs').get('VolumeId'))
            return print(f"Snapshots are being created, check EC2 console")
