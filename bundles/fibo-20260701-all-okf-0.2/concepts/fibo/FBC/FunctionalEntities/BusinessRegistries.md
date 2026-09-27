---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the Registration Authorities ontology to define specific kinds of registries, such as business
      entity registries, registries for identifiers and codes of various sorts, and registries for financial institutions
      and intermediaries based on jurisdiction, who regulates them, and the services they provide.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2020-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
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
    value: Business Registries Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was modified per the issue resolutions identified in the FIBO FBC 1.1 RTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was modified per FIBO 2.0 RFC primarily to loosen the constraints on address properties and better support
      standards including ISO 9362 (BIC codes), ISO 13616 (IBAN and BBAN codes), and ISO 17442 (the GLIEF LEI standard).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was modified to generalize certain unions where they were no longer required, use the composite date datatype
      where appropriate, add individuals for entity expiration reason and validation level to better align with the GLEIF
      LEI data, and move international registration authorities, such as SWIFT, to a separate ontology for better modularity.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to eliminate duplication with concepts in LCC, simplify addresses, normalize definitions to
      be ISO 704 compliant, and rationalize address properties.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of
      datatypes in the Relations concept is not needed here.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to eliminate circular and ambiguous definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210201/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210901/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to clarify the definition of registry identifier and augment the definitions of certain identifiers,
      such as an LEI, to make them registry identifiers, as well as to modify the definition of an LOU to be a Registrar rather
      than RegistrationAuthority, and deprecate the redundant LOU identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to eliminate deprecated content.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220501/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was revised to eliminate dead links and address text formatting issues uncovered by hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary and refine the definitions of certain date properties to allow for broader usage,
      such as for market-related content.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/BusinessRegistries.rdf version of
      this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1
      (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons)
      v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency
      and useability (BE-259).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to augment details related to GLEIF LEI records as needed to extend examples (FND-407).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20260601/FunctionalEntities/BusinessRegistries.rdf version of
      the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent
      in OMG Commons (FND-412).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/LegalEntities/LEIEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/BusinessRegistries/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FND/AgentsAndPeople/People.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/Places/Addresses.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/
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
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: Business Registries Ontology
type: Ontology Definition
---

# Business Registries Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/>

## Relationships

- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [LEIEntities](/concepts/fibo/BE/LegalEntities/LEIEntities.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [People](/concepts/fibo/FND/AgentsAndPeople/People.md)
- **Related to**: [ClassificationSchemes](/concepts/fibo/FND/Arrangements/ClassificationSchemes.md)
- **Related to**: [Addresses](/concepts/fibo/FND/Places/Addresses.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [DatesAndTimes](<https://www.omg.org/spec/Commons/DatesAndTimes/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [BusinessRegistries](<https://spec.edmcouncil.org/fibo/ontology/FBC/20260701/FunctionalEntities/BusinessRegistries/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the Registration Authorities ontology to define specific kinds of registries, such as business entity registries, registries for identifiers and codes of various sorts, and registries for financial institutions and intermediaries based on jurisdiction, who regulates them, and the services they provide.
- **license**: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2020-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Business Registries Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/BusinessRegistries.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FBC 1.1 RTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/BusinessRegistries.rdf version of this ontology was modified per FIBO 2.0 RFC primarily to loosen the constraints on address properties and better support standards including ISO 9362 (BIC codes), ISO 13616 (IBAN and BBAN codes), and ISO 17442 (the GLIEF LEI standard).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/BusinessRegistries.rdf version of this ontology was modified to generalize certain unions where they were no longer required, use the composite date datatype where appropriate, add individuals for entity expiration reason and validation level to better align with the GLEIF LEI data, and move international registration authorities, such as SWIFT, to a separate ontology for better modularity.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190501/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to replace hasDefinition with isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190701/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to eliminate duplication with concepts in LCC, simplify addresses, normalize definitions to be ISO 704 compliant, and rationalize address properties.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200301/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes in the Relations concept is not needed here.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20200701/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to eliminate circular and ambiguous definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210201/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to reflect the move of certain organization-specific concepts from BE to FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210901/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to clarify the definition of registry identifier and augment the definitions of certain identifiers, such as an LEI, to make them registry identifiers, as well as to modify the definition of an LOU to be a Registrar rather than RegistrationAuthority, and deprecate the redundant LOU identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20211201/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to eliminate deprecated content.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220501/FunctionalEntities/BusinessRegistries.rdf version of this ontology was revised to eliminate dead links and address text formatting issues uncovered by hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary and refine the definitions of certain date properties to allow for broader usage, such as for market-related content.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/BusinessRegistries.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20231101/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to merge details from the old corporations ontology into corporate bodies for consistency and useability (BE-259).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to augment details related to GLEIF LEI records as needed to extend examples (FND-407).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20260601/FunctionalEntities/BusinessRegistries.rdf version of the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons (FND-412).
- **copyright**: Copyright (c) 2020-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2020-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
