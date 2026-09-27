---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the primary financial services entities ontology in FBC with additional kinds of entities
      that are specific to the United States.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2025 EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group, Inc.\n\nPermission\
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
    value: US Financial Services Entities Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified per the issue resolutions identified in the FIBO FBC 1.0 FTF report.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to generalize the definition of credit union.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to eliminate circular definitions and revise names such that concepts don't appear
      to refer to multiple things.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210201/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to eliminate dead links and address text formatting issues identified through
      hygiene testing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than
      the OMG's Specification Metadata vocabulary, add additional kinds of institutions in order to answer competency questions
      using the National Information Center (NIC) repository, leverage the Commons Ontology Library (Commons) rather than
      the OMG's Languages, Countries and Codes (LCC) to eliminate redundancies in FIBO, and clean up a couple of definitions
      to be ISO 704 compliant.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to augment the representation of institutions based on their definitions in the
      law, in order to answer competency questions using the National Information Center (NIC) repository
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons)
      v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology
      Library (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
      version of the ontology was modified to to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
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
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: US Financial Services Entities Ontology
type: Ontology Definition
---

# US Financial Services Entities Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/>

## Relationships

- **Related to**: [USGovernmentEntitiesAndJurisdictions](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions.md)
- **Related to**: [CorporateBodies](/concepts/fibo/BE/LegalEntities/CorporateBodies.md)
- **Related to**: [FormalBusinessOrganizations](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations.md)
- **Related to**: [CorporateControl](/concepts/fibo/BE/OwnershipAndControl/CorporateControl.md)
- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [Control](/concepts/fibo/FND/OwnershipAndControl/Control.md)
- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SitesAndFacilities](<https://www.omg.org/spec/Commons/SitesAndFacilities/>)
- **Related to**: [ISO3166-1-CountryCodes](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/>)
- **Related to**: [USFinancialServicesEntities](<https://spec.edmcouncil.org/fibo/ontology/FBC/20251201/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the primary financial services entities ontology in FBC with additional kinds of entities that are specific to the United States.
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: US Financial Services Entities Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20150801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FBC 1.0 FTF report.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20160801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to generalize the definition of credit union.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20190901/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to eliminate circular definitions and revise names such that concepts don't appear to refer to multiple things.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210201/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to eliminate dead links and address text formatting issues identified through hygiene testing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20220801/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary, add additional kinds of institutions in order to answer competency questions using the National Information Center (NIC) repository, leverage the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) to eliminate redundancies in FIBO, and clean up a couple of definitions to be ISO 704 compliant.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230301/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to augment the representation of institutions based on their definitions in the law, in order to answer competency questions using the National Information Center (NIC) repository
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230401/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of this ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20240101/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf version of the ontology was modified to to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
