# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class AssignAlertRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, user=None, note=None, source=None, owner=None):
        """
        AssignAlertRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'str',
            'note': 'str',
            'source': 'str',
            'owner': 'UserRecipient'
        }

        self.attribute_map = {
            'user': 'user',
            'note': 'note',
            'source': 'source',
            'owner': 'owner'
        }

        self._user = user
        self._note = note
        self._source = source
        self._owner = owner

    @property
    def user(self):
        """
        Gets the user of this AssignAlertRequest.
        Display name of the request owner

        :return: The user of this AssignAlertRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AssignAlertRequest.
        Display name of the request owner

        :param user: The user of this AssignAlertRequest.
        :type: str
        """

        self._user = user

    @property
    def note(self):
        """
        Gets the note of this AssignAlertRequest.
        Additional note that will be added while creating the alert

        :return: The note of this AssignAlertRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this AssignAlertRequest.
        Additional note that will be added while creating the alert

        :param note: The note of this AssignAlertRequest.
        :type: str
        """

        self._note = note

    @property
    def source(self):
        """
        Gets the source of this AssignAlertRequest.
        Source field of the alert. Default value is IP address of the incoming request

        :return: The source of this AssignAlertRequest.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this AssignAlertRequest.
        Source field of the alert. Default value is IP address of the incoming request

        :param source: The source of this AssignAlertRequest.
        :type: str
        """

        self._source = source

    @property
    def owner(self):
        """
        Gets the owner of this AssignAlertRequest.

        :return: The owner of this AssignAlertRequest.
        :rtype: UserRecipient
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this AssignAlertRequest.

        :param owner: The owner of this AssignAlertRequest.
        :type: UserRecipient
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AssignAlertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other