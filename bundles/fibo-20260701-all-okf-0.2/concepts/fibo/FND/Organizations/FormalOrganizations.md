---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the Commons concept of a formal organization, which is purposefully underspecified to facilitate
      mapping to other organization ontologies, such as the W3C organization ontology, or others defined for specific business
      and financial services standards. It also defines general concepts related to employment by a formal organization.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\t\t\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Formal Organizations Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Organizations/FormalOrganizations.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/.
      It was further revised in the FTF in advance of the Long Beach meeting, resulting in http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Organizations/FormalOrganizations/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Organizations/FormalOrganizations.rdf version of this ontology
      was modified per the FIBO 2.0 RFC to integrate concepts from LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Organizations/FormalOrganizations.owl version of the ontology\
      \ was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n\t(1) to use slash style URI/IRIss\
      \ (also called 303 URIs, vs. hash style) as required to support server side processing \n\t(2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n\t(3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n\t(4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n\t(5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Organizations/FormalOrganizations.rdf version of this
      ontology was revised to loosen the constraints on the range of isDomiciledIn, allow for multiple values, update definitions
      to be ISO 704 compliant, and eliminate duplication with concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Organizations/FormalOrganizations.rdf version of this
      ontology was revised to incorporate the concept of employment, required to support regulatory reporting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Organizations/FormalOrganizations.rdf version of this
      ontology was revised to address hygiene issues with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Organizations/FormalOrganizations.rdf version of the
      ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Organizations/FormalOrganizations.rdf version of this
      ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes
      (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Organizations/FormalOrganizations.rdf version of this
      ontology was modified to loosen the domain of 'is domiciled in' to include organization sub-units, such as branches
      and divisions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230401/Organizations/FormalOrganizations.rdf version of this
      ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Organizations/FormalOrganizations.rdf version of the
      ontology was modified to eliminate elements that have been deprecated for more than 3 quarters (FND-399).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Organizations/FormalOrganizations.rdf version of the
      ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Organizations/FormalOrganizations.rdf version of the
      ontology was modified to move a restriction on the agent class to this ontology, allowing eliminatation of the agents
      ontology to simplify imports. (FND-411).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Organizations/FormalOrganizations/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/
sources:
- id: fibo-source-aa59b20c83
  resource: references/fibo/FND/Organizations/FormalOrganizations.rdf
  sha256: aa59b20c83dd0996c31db301142a4e02ff283400d1609f21b5b9904d450c717b
  title: FIBO source FND/Organizations/FormalOrganizations.rdf
title: Formal Organizations Ontology
type: Ontology Definition
---

# Formal Organizations Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/>

## Relationships

- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [FormalOrganizations](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Organizations/FormalOrganizations/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the Commons concept of a formal organization, which is purposefully underspecified to facilitate mapping to other organization ontologies, such as the W3C organization ontology, or others defined for specific business and financial services standards. It also defines general concepts related to employment by a formal organization.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Formal Organizations Ontology
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20130801/Organizations/FormalOrganizations.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in http://www.omg.org/spec/EDMC-FIBO/FND/1.0/AboutFND-1.0/. It was further revised in the FTF in advance of the Long Beach meeting, resulting in http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Organizations/FormalOrganizations/.
- **changeNote**: The http://www.omg.org/spec/EDMC-FIBO/FND/20141101/Organizations/FormalOrganizations.rdf version of this ontology was modified per the FIBO 2.0 RFC to integrate concepts from LCC.
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Organizations/FormalOrganizations.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows: 	(1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing  	(2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs 	(3) to change the file suffix from .owl to .rdf to increase usability in RDF tools 	(4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure 	(5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Organizations/FormalOrganizations.rdf version of this ontology was revised to loosen the constraints on the range of isDomiciledIn, allow for multiple values, update definitions to be ISO 704 compliant, and eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/Organizations/FormalOrganizations.rdf version of this ontology was revised to incorporate the concept of employment, required to support regulatory reporting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Organizations/FormalOrganizations.rdf version of this ontology was revised to address hygiene issues with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Organizations/FormalOrganizations.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Organizations/FormalOrganizations.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Organizations/FormalOrganizations.rdf version of this ontology was modified to loosen the domain of 'is domiciled in' to include organization sub-units, such as branches and divisions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230401/Organizations/FormalOrganizations.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Organizations/FormalOrganizations.rdf version of the ontology was modified to eliminate elements that have been deprecated for more than 3 quarters (FND-399).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/Organizations/FormalOrganizations.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20251201/Organizations/FormalOrganizations.rdf version of the ontology was modified to move a restriction on the agent class to this ontology, allowing eliminatation of the agents ontology to simplify imports. (FND-411).
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
