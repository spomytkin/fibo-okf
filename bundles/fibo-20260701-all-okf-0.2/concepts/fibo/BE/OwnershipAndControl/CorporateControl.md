---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts relating to corporation-specific control. These concepts are based on the general
      types of control (both de facto control and controlling interests), as defined in the ControlParties ontology, and are
      the specific examples of these concepts as they apply to companies incorporated by the issuance of shares.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\n\t\tCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\t\
      \tPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Corporate Control Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/CorporateControl.rdf version of this
      ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/CorporateControl.rdf version of this
      ontology was modified per the FIBO 2.0 RFC to add missing definitions and labels, eliminate references to BusinessFacingTypes,
      replace min 1 QCRs with someValuesFrom, address other hygiene issues, and limit the burden of certain restrictions,
      such as those on stock corporation, for typical applications.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/CorporateControl.rdf version of this
      ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to correct reasoning
      anomalies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/OwnershipAndControl/CorporateControl.rdf version of this
      ontology was revised to allow any legal entity to participate in control relations rather than limiting control to a
      stock corporation, and simplifying others such that any party can be a significant shareholder, for example, rather
      than limiting this role to a legal entity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200501/OwnershipAndControl/CorporateControl.rdf version of this
      ontology was revised to further clean up definitions related to control via ownership of shares, which only applies
      to corporations and some partnerships, and revise and extend the definition of affiliation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to simplify control concepts and relations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to incorporate the latest insights into how control relations should integrate with the control
      situation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to address text formatting hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/CorporateControl.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/CorporateControl/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: Corporate Control Ontology
type: Ontology Definition
---

# Corporate Control Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [ControlParties](/concepts/fibo/BE/OwnershipAndControl/ControlParties.md)
- **Related to**: [CorporateOwnership](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership.md)
- **Related to**: [OwnershipParties](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [CorporateControl](<https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/CorporateControl/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts relating to corporation-specific control. These concepts are based on the general types of control (both de facto control and controlling interests), as defined in the ControlParties ontology, and are the specific examples of these concepts as they apply to companies incorporated by the issuance of shares.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. 		Copyright (c) 2013-2025 Object Management Group, Inc. 		 		Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Corporate Control Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/CorporateControl.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/CorporateControl.rdf version of this ontology was modified per the FIBO 2.0 RFC to add missing definitions and labels, eliminate references to BusinessFacingTypes, replace min 1 QCRs with someValuesFrom, address other hygiene issues, and limit the burden of certain restrictions, such as those on stock corporation, for typical applications.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/CorporateControl.rdf version of this ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to correct reasoning anomalies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190101/OwnershipAndControl/CorporateControl.rdf version of this ontology was revised to allow any legal entity to participate in control relations rather than limiting control to a stock corporation, and simplifying others such that any party can be a significant shareholder, for example, rather than limiting this role to a legal entity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200501/OwnershipAndControl/CorporateControl.rdf version of this ontology was revised to further clean up definitions related to control via ownership of shares, which only applies to corporations and some partnerships, and revise and extend the definition of affiliation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to simplify control concepts and relations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to incorporate the latest insights into how control relations should integrate with the control situation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to address text formatting hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/CorporateControl.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
