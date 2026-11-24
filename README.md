# Collection: my_own_namespace.yandex_cloud_elk

This collection contains a custom Ansible module `my_own_module` and a role `my_role` that uses it.

## Module: my_own_module

Creates a text file on a remote host with specified content.

### Parameters:
* `path` (required): Path to the file.
* `content` (required): Content to write into the file.

### Example:
```yaml
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello, Netology!"
```

## Role: my_role

Uses the `my_own_module` to create a file with default parameters.

### Defaults:
* `my_file_path`: `/tmp/default_path.txt`
* `my_file_content`: `"Default content from role"`
