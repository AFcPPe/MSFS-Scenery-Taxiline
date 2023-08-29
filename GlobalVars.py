outer = '''<?xml version="1.0"?>
<FSData version="9.0">
    <Airport displayName="{0}" groupIndex="1" groupID="1" groupGenerated="FALSE" name="{0}" ident="{1}" lat="{2}" lon="{3}" alt="{4}" magvar="0.000000" trafficScalar="1.000000" airportTestRadius="2540.20069524900282" applyFlatten="FALSE" isOnTIN="FALSE" tinColorCorrection="TRUE">
        {5}
    </Airport>
</FSData>'''

tPoint = '<TaxiwayPoint parentGroupID="1" groupIndex="{0}" index="{1}" type="NORMAL" orientation="FORWARD" lat="{2}" lon="{3}"/>'

tPath = '<TaxiwayPath parentGroupID="1" groupIndex="{0}" type="TAXI" surface="{{85D02B2B-08A1-452E-AB07-6D5AE7F52884}}" centerLine="TRUE" centerLineLighted="TRUE" start="{1}" end="{2}" width="30.000000" weightLimit="0" name="0" drawSurface="TRUE" drawDetail="TRUE" groundMerging="TRUE" excludeVegetationAround="TRUE" excludeVegetationInside="TRUE"/>'
