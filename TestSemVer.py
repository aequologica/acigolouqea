#!/usr/bin/env python
import semantic_version

def test(version):
    """
    Increment a semantic version

    :param version: str of the version to increment
    :param major: bool specifying major level version increment
    :param minor: bool specifying minor level version increment
    :param patch: bool specifying patch level version increment
    :return: str of the incremented version
    """
    v = semantic_version.Version(str(version))
    
    print(v.major);
    print(v.minor);
    print(v.patch);
    print(v.prerelease);
    print(v.build);

    return version

test('2.0.0-rc.4+SNAPSHOT')
