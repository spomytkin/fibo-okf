---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts relating to types of organization owning parties. The concepts defined here are
      party in role concepts, which define the nature of some entity such as an organization or a legal person, in some role
      such as that of owning equity in the entity. These roles are defined in terms of the ownership enjoyed by the party,
      with distinctions between constitutional ownership i.e. ownership defined in terms of stockholder equity, and investment
      ownership more generally.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Ownership Parties Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified per the FIBO 2.0 RFC to address missing labels and comments, and revise terminology related to
      shareholders' equity due to requirements for SEC/Equities.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to support GLEIF
      LEI Level 2 ownership relationships.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20181201/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to eliminate duplication of concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to integrate the concept of a situation, situational roles, and corresponding relations with the
      definition of entity ownership, and eliminate unused and logically inconsistent properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was revised to reflect the name change in FND from 'hasPrimaryParty' to 'hasActiveParty' to be more consistent
      with other role related properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200701/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was revised to align isEquityHeldBy and hasInvestor with the situational pattern.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was revised to eliminate references to guarantee providing member, which duplicates the concept of a guarantor
      and references a concept that is no longer needed, namely 'body incorporated with guarantee'.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was revised to add a restriction on entity ownership for the ownership percentage.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was revised to eliminate a dead link that was not necessary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/OwnershipAndControl/OwnershipParties.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons
      Ontology Library (Commons) v1.1 and clean up a few definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20231201/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to replace additional concepts from FIBO FND with their counterparts added to the Commons Ontology
      Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/OwnershipParties.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to add a parent class of contract party to the definition of investory (SEC-113).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/OwnershipParties.rdf version of this
      ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/OwnershipParties/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: Ownership Parties Ontology
type: Ontology Definition
---

# Ownership Parties Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/>

## Relationships

- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [OwnershipParties](<https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/OwnershipParties/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts relating to types of organization owning parties. The concepts defined here are party in role concepts, which define the nature of some entity such as an organization or a legal person, in some role such as that of owning equity in the entity. These roles are defined in terms of the ownership enjoyed by the party, with distinctions between constitutional ownership i.e. ownership defined in terms of stockholder equity, and investment ownership more generally.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **label**: Ownership Parties Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20131101/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20160201/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified per the FIBO 2.0 RFC to address missing labels and comments, and revise terminology related to shareholders' equity due to requirements for SEC/Equities.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180801/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified as a part of a simplification strategy for the organizational class hierarchy and to support GLEIF LEI Level 2 ownership relationships.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20181201/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190901/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to eliminate duplication of concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200201/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to integrate the concept of a situation, situational roles, and corresponding relations with the definition of entity ownership, and eliminate unused and logically inconsistent properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200601/OwnershipAndControl/OwnershipParties.rdf version of this ontology was revised to reflect the name change in FND from 'hasPrimaryParty' to 'hasActiveParty' to be more consistent with other role related properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200701/OwnershipAndControl/OwnershipParties.rdf version of this ontology was revised to align isEquityHeldBy and hasInvestor with the situational pattern.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200901/OwnershipAndControl/OwnershipParties.rdf version of this ontology was revised to eliminate references to guarantee providing member, which duplicates the concept of a guarantor and references a concept that is no longer needed, namely 'body incorporated with guarantee'.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20201201/OwnershipAndControl/OwnershipParties.rdf version of this ontology was revised to add a restriction on entity ownership for the ownership percentage.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210401/OwnershipAndControl/OwnershipParties.rdf version of this ontology was revised to eliminate a dead link that was not necessary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20220801/OwnershipAndControl/OwnershipParties.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1 and clean up a few definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20231201/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to replace additional concepts from FIBO FND with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/OwnershipParties.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to add a parent class of contract party to the definition of investory (SEC-113).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/OwnershipAndControl/OwnershipParties.rdf version of this ontology was modified to reflect migration of concepts from accounting equity to ownership in FND (FND-409).
- **copyright**: Copyright (c) 2013-2025 Object Management Group
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
