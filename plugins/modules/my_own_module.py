#!/usr/bin/python

# Copyright: (c) 2026, Sergey Meshkov <example@example.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my custom module to create text files

version_added: "1.0.0"

description: This module creates a text file on a remote host with specified content.

options:
    path:
        description: The path where the file should be created (e.g., /tmp/test.txt).
        required: true
        type: str
    content:
        description: The content to write into the file.
        required: true
        type: str

author:
    - Sergey Meshkov (@meshkov-sergey)
'''

EXAMPLES = r'''
# Create a file with content
- name: Create a text file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test.txt
    content: "Hello, Netology!"

# Create another file with different content
- name: Create another file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/test2.txt
    content: "Ansible is awesome"
'''

RETURN = r'''
# These are examples of possible return values.
path:
    description: The path where the file was created.
    type: str
    returned: always
    sample: '/tmp/test.txt'
content:
    description: The content that was written.
    type: str
    returned: always
    sample: 'Hello, Netology!'
'''

from ansible.module_utils.basic import AnsibleModule
import os


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    # seed the result dict in the object
    result = dict(
        changed=False,
        path='',
        content=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # get parameters
    path = module.params['path']
    content = module.params['content']

    # check if file exists and has the same content
    file_exists = os.path.exists(path)
    content_matches = False

    if file_exists:
        with open(path, 'r') as f:
            current_content = f.read()
            if current_content == content:
                content_matches = True

    # if file doesn't exist or content differs, we need to write it
    if not file_exists or not content_matches:
        result['changed'] = True
        try:
            with open(path, 'w') as f:
                f.write(content)
        except Exception as e:
            module.fail_json(msg=f"Failed to write file: {e}", **result)

    # fill return values
    result['path'] = path
    result['content'] = content

    # in the event of a successful module execution, exit with json
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
