---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines concepts and primarily individuals required to identify securities, including the individuals
      that represent a number of well-known securities identifiers and related schemes, registries, and registration authorities.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2016-2025 Object Management Group,\
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
    value: Securities Identification Individuals Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Securities/SecuritiesIdentification/ version of this
      ontology was modified to correct several logic issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190601/Securities/SecuritiesIdentification/ version of this
      ontology was updated to represent identifiers as classes rather than individuals and rename (migrate) the hasDefinition
      property to isDefinedIn to clarify intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190701/Securities/SecuritiesIdentificationIndividuals/ version
      of this ontology was modified to restructure the concept of a listing and augment it with a number of relevant characteristics.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Securities/SecuritiesIdentificationIndividuals/ version
      of this ontology was modified to eliminate duplication of concepts with LCC and eliminate punning in individual definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Securities/SecuritiesIdentificationIndividuals/ version
      of this ontology was modified to replace 'characterizes' with 'describes', which more accurately expresses the intent.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200701/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to eliminate confusion between listed security and listing (which caused reasoning issues)
      and add the Telekurs Id (now retired) and Valoren as securities identifiers.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to correct a bad character in a note on the Valoren.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210201/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to eliminate punning with respect to the FIGI registry entry.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211201/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to correct a typo in an annotation property name.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to address text formatting hygiene issues and clean up dead or irrelevant links.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was revised to replace 'financial information publisher' with 'publisher'.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221001/Securities/SecuritiesIdentificationIndividuals.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was modified to revise the representation of a RIC code to reflect that it is now published by the
      London Stock Exchange and is branded using their Refinitiv brand (SEC-196).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240401/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was modified to address a punning issue (GitHub-2040).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240901/Securities/SecuritiesIdentificationIndividuals.rdf version
      of this ontology was modified to eliminate elements that have been deprecated for over six months (FND-386).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241101/Securities/SecuritiesIdentificationIndividuals.rdf version
      of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Securities/SecuritiesIdentificationIndividuals.rdf version
      of the ontology was modified to refine and streamline the definitions of some service providers (SEC-205).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251001/Securities/SecuritiesIdentificationIndividuals.rdf version
      of the ontology was modified to reflect the migration of registration authorities to the Functional Entities module
      in FBC and better align with the GLEIF LEI model (FND-407).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/
  - concept: /concepts/fibo/BE/FunctionalEntities/Publishers.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/
  - concept: /concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/
  - concept: /concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - concept: /concepts/fibo/IND/InterestRates/MarketDataProviders.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/MarketDataProviders/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/20260601/Securities/SecuritiesIdentificationIndividuals/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Securities Identification Individuals Ontology
type: Ontology Definition
---

# Securities Identification Individuals Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/>

## Relationships

- **Related to**: [FunctionalEntities](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities.md)
- **Related to**: [Publishers](/concepts/fibo/BE/FunctionalEntities/Publishers.md)
- **Related to**: [GovernmentEntities](/concepts/fibo/BE/GovernmentEntities/GovernmentEntities.md)
- **Related to**: [FinancialInstruments](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments.md)
- **Related to**: [CommercialRegistrationAuthorities](/concepts/fibo/FBC/FunctionalEntities/CommercialRegistrationAuthorities.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [MarketDataProviders](/concepts/fibo/IND/InterestRates/MarketDataProviders.md)
- **Related to**: [SecuritiesIdentification](/concepts/fibo/SEC/Securities/SecuritiesIdentification.md)
- **Related to**: [SecuritiesListings](/concepts/fibo/SEC/Securities/SecuritiesListings.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegistrationAuthorities](<https://www.omg.org/spec/Commons/RegistrationAuthorities/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SecuritiesIdentificationIndividuals](<https://spec.edmcouncil.org/fibo/ontology/SEC/20260601/Securities/SecuritiesIdentificationIndividuals/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines concepts and primarily individuals required to identify securities, including the individuals that represent a number of well-known securities identifiers and related schemes, registries, and registration authorities.
- **license**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2016-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Securities Identification Individuals Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20180801/Securities/SecuritiesIdentification/ version of this ontology was modified to correct several logic issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190601/Securities/SecuritiesIdentification/ version of this ontology was updated to represent identifiers as classes rather than individuals and rename (migrate) the hasDefinition property to isDefinedIn to clarify intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20190701/Securities/SecuritiesIdentificationIndividuals/ version of this ontology was modified to restructure the concept of a listing and augment it with a number of relevant characteristics.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20191201/Securities/SecuritiesIdentificationIndividuals/ version of this ontology was modified to eliminate duplication of concepts with LCC and eliminate punning in individual definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200301/Securities/SecuritiesIdentificationIndividuals/ version of this ontology was modified to replace 'characterizes' with 'describes', which more accurately expresses the intent.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20200701/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to eliminate confusion between listed security and listing (which caused reasoning issues) and add the Telekurs Id (now retired) and Valoren as securities identifiers.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20201201/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to correct a bad character in a note on the Valoren.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20210201/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to eliminate punning with respect to the FIGI registry entry.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20211201/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to correct a typo in an annotation property name.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to address text formatting hygiene issues and clean up dead or irrelevant links.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20220101/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was revised to replace 'financial information publisher' with 'publisher'.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20221001/Securities/SecuritiesIdentificationIndividuals.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230201/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20230301/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20231201/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was modified to revise the representation of a RIC code to reflect that it is now published by the London Stock Exchange and is branded using their Refinitiv brand (SEC-196).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240401/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was modified to address a punning issue (GitHub-2040).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20240901/Securities/SecuritiesIdentificationIndividuals.rdf version of this ontology was modified to eliminate elements that have been deprecated for over six months (FND-386).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20241101/Securities/SecuritiesIdentificationIndividuals.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20250301/Securities/SecuritiesIdentificationIndividuals.rdf version of the ontology was modified to refine and streamline the definitions of some service providers (SEC-205).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/SEC/20251001/Securities/SecuritiesIdentificationIndividuals.rdf version of the ontology was modified to reflect the migration of registration authorities to the Functional Entities module in FBC and better align with the GLEIF LEI model (FND-407).
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
