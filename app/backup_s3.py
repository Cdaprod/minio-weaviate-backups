result = client.backup.create(
  backup_id="backup-id-2",
  backend="s3",
  include_classes=["Article", "Author"],  # specify classes to include or omit this for all classes
  wait_for_completion=True,
)
print(result)