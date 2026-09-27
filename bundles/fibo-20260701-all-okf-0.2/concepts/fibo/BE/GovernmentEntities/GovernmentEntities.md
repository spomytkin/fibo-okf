---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines the fundamental concepts for representing polities and government entities and their relations.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2025 EDM Council, Inc.\nCopyright (c) 2016-2025 Object Management Group, Inc.\n\t\t\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Government Entities Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/BE/20160801/GovernmentEntities/GovernmentEntities.rdf version of this ontology
      was added to Business Entities, per the issue resolutions identified in the FIBO BE 1.1 RTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/BE/20160801/GovernmentEntities/GovernmentEntities.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO BE 1.2 RTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/BE/20170201/GovernmentEntities/GovernmentEntities.rdf version of this ontology
      was modified per the FIBO 2.0 RFC to integrate LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20180201/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to to rationalize natural person and legally capable person in a new concept, competent natural
      person, simplify / merge the legal person and formal organization class hierarchies, and revise certain definitions,
      such as for supranational entity, to correspond to ISO definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20181201/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to reflect the move of hasObjective to FND to enable higher level reuse and eliminate a reasoning
      error.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20190501/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to eliminate duplication of concepts in LCC and merge the countries ontology with locations.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200301/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to replace isAppointedBy with isDesignatedBy due to a name change in Relations, and to add
      a class for devolved government.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20200701/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to eliminate references to external dictionary sites that no longer resolve, revise circular
      or ambiguous definitions, and to eliminate 'hasPartialSovereigntyOver' in favor of 'hasSharedSovereigntyOver'.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20210201/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to fix spelling errors.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to address text formatting hygiene issues and to use the Commons Ontology Library (Commons)
      Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to augment the definition of instrumentality with additional notes.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20230901/GovernmentEntities/GovernmentEntities.rdf version of
      this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      and loosened restrictions causing reasoning and representational challenges (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/GovernmentEntities/GovernmentEntities.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/GovernmentEntities/GovernmentEntities.rdf version of
      the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396) and to
      further reflect changes made in Commons v1.2 (FBC-338).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/GovernmentEntities/GovernmentEntities.rdf version of
      the ontology was modified to remove deprecations that reflect changes made in Commons v1.2 (FBC-399) and to use new
      constructs from the Commons 1.3 Business Authorizations ontology (FND-401).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/20251201/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Law/LegalCore.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/
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
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
sources:
- id: fibo-source-5deab1a754
  resource: references/fibo/BE/GovernmentEntities/GovernmentEntities.rdf
  sha256: 5deab1a75487a8f7ff902b567d86099df6c1e24acc1a3a06d0351785ed1d30d3
  title: FIBO source BE/GovernmentEntities/GovernmentEntities.rdf
title: Government Entities Ontology
type: Ontology Definition
---

# Government Entities Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [Executives](/concepts/fibo/BE/OwnershipAndControl/Executives.md)
- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [LegalCore](/concepts/fibo/FND/Law/LegalCore.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [BusinessAuthorizations](<https://www.omg.org/spec/Commons/BusinessAuthorizations/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [GovernmentEntities](<https://spec.edmcouncil.org/fibo/ontology/BE/20251201/GovernmentEntities/GovernmentEntities/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines the fundamental concepts for representing polities and government entities and their relations.
- **license**: Copyright (c) 2016-2025 EDM Council, Inc. Copyright (c) 2016-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Government Entities Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/BE/20160801/GovernmentEntities/GovernmentEntities.rdf version of this ontology was added to Business Entities, per the issue resolutions identified in the FIBO BE 1.1 RTF report.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/BE/20160801/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified per the issue resolutions identified in the FIBO BE 1.2 RTF report.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/BE/20170201/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified per the FIBO 2.0 RFC to integrate LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20180201/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to to rationalize natural person and legally capable person in a new concept, competent natural person, simplify / merge the legal person and formal organization class hierarchies, and revise certain definitions, such as for supranational entity, to correspond to ISO definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20181201/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to reflect the move of hasObjective to FND to enable higher level reuse and eliminate a reasoning error.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20190501/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to eliminate duplication of concepts in LCC and merge the countries ontology with locations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200301/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to replace isAppointedBy with isDesignatedBy due to a name change in Relations, and to add a class for devolved government.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20200701/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to eliminate references to external dictionary sites that no longer resolve, revise circular or ambiguous definitions, and to eliminate 'hasPartialSovereigntyOver' in favor of 'hasSharedSovereigntyOver'.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20210201/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to fix spelling errors.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20211201/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to address text formatting hygiene issues and to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230101/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230301/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to augment the definition of instrumentality with additional notes.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20230901/GovernmentEntities/GovernmentEntities.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 and loosened restrictions causing reasoning and representational challenges (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20240101/GovernmentEntities/GovernmentEntities.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20250301/GovernmentEntities/GovernmentEntities.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396) and to further reflect changes made in Commons v1.2 (FBC-338).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/BE/20251001/GovernmentEntities/GovernmentEntities.rdf version of the ontology was modified to remove deprecations that reflect changes made in Commons v1.2 (FBC-399) and to use new constructs from the Commons 1.3 Business Authorizations ontology (FND-401).
- **copyright**: Copyright (c) 2016-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
