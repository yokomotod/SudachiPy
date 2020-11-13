# Copyright (c) 2019 Works Applications Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# the first version of system dictionaries
SYSTEM_DICT_VERSION_1 = 0x7366d3f18bd111e7

# the second version of system dictionaries
SYSTEM_DICT_VERSION_2 = 0xce9f011a92394434

USER_DICT_VERSION_1 = 0xa50f31188bd211e7
USER_DICT_VERSION_2 = 0x9fdeb5a90168d868


def is_system_dictionary(version):
    return version == SYSTEM_DICT_VERSION_1 or version == SYSTEM_DICT_VERSION_2


def is_user_dictionary(version):
    return version == USER_DICT_VERSION_1 or version == USER_DICT_VERSION_2
