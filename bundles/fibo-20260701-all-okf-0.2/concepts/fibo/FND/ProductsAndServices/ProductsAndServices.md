---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines fundamental concepts for buyers, sellers, clients, customers, products, goods and services
      for use in other FIBO ontologies.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2025 EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\nPermission\
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
    value: Products and Services Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20150801/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report to replace MoneyAmount
      with AmountOfMoney.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was modified for the FIBO 2.0 RFC to add NegotiableCommodity and Consumer.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was modified to include classes to support automated inclusion of all ISO 4217 codes published as of
      2018-06-04.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was modified to move (deprecate) the properties produces and isProducedBy to Relations for more general
      usability.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to leverage the new party identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to eliminate duplication with concepts in LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union
      of datatypes in the Relations concept is not needed here.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to add properties for hasBuyer and hasSeller, integrate properties with the party lattice,
      and clean-up circular or ambiguous definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to incorporate the concept of a right into the definition of product, to cover leases and
      rentals, such as the right to use a piece of property or other asset for some period of time, as products.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised move the definition of precious metal and the corresponding identifier to CurrencyAmount
      from this ontology to simplify imports in cases where the broader definitions for commodities are not required.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220201/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was revised to eliminate deprecated elements related to precious metals.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's
      Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/ProductsAndServices/ProductsAndServices.rdf version
      of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries
      and Codes (LCC), eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the
      Commons Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts
      added to the Commons Ontology Library (Commons) v1.1.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to replace the definition of real estate with the new definition in the real property ontology
      (LOAN-168).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library
      (Commons) v1.2 (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to simplify the agreements class hierarchy (FND-391).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250501/ProductsAndServices/ProductsAndServices.rdf version
      of the ontology was modified to eliminate long-deprecated content (FND-399) and to reuse concepts from the Commons 1.3
      sites and facilities ontology (FND-401).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20251201/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/
  - concept: /concepts/fibo/FND/Law/LegalCapacity.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/
  - concept: /concepts/fibo/FND/Parties/Parties.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/
  - concept: /concepts/fibo/FND/Places/RealProperty.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/
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
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/SitesAndFacilities/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: Products and Services Ontology
type: Ontology Definition
---

# Products and Services Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/>

## Relationships

- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [Occurrences](/concepts/fibo/FND/DatesAndTimes/Occurrences.md)
- **Related to**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity.md)
- **Related to**: [Parties](/concepts/fibo/FND/Parties/Parties.md)
- **Related to**: [RealProperty](/concepts/fibo/FND/Places/RealProperty.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [PartiesAndSituations](<https://www.omg.org/spec/Commons/PartiesAndSituations/>)
- **Related to**: [RegulatoryAgencies](<https://www.omg.org/spec/Commons/RegulatoryAgencies/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [SitesAndFacilities](<https://www.omg.org/spec/Commons/SitesAndFacilities/>)
- **Related to**: [ProductsAndServices](<https://spec.edmcouncil.org/fibo/ontology/FND/20251201/ProductsAndServices/ProductsAndServices/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines fundamental concepts for buyers, sellers, clients, customers, products, goods and services for use in other FIBO ontologies.
- **license**: Copyright (c) 2013-2025 EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Products and Services Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20150801/ProductsAndServices/ProductsAndServices.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report to replace MoneyAmount with AmountOfMoney.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/ProductsAndServices/ProductsAndServices.rdf version of this ontology was modified for the FIBO 2.0 RFC to add NegotiableCommodity and Consumer.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/ProductsAndServices/ProductsAndServices.rdf version of this ontology was modified to include classes to support automated inclusion of all ISO 4217 codes published as of 2018-06-04.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/ProductsAndServices/ProductsAndServices.rdf version of this ontology was modified to move (deprecate) the properties produces and isProducedBy to Relations for more general usability.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to leverage the new party identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190701/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to eliminate duplication with concepts in LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200201/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to replace uses of hasTag in Relations with hasTag from LCC, as the more complex union of datatypes in the Relations concept is not needed here.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200701/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to add properties for hasBuyer and hasSeller, integrate properties with the party lattice, and clean-up circular or ambiguous definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210101/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to incorporate the concept of a right into the definition of product, to cover leases and rentals, such as the right to use a piece of property or other asset for some period of time, as products.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised move the definition of precious metal and the corresponding identifier to CurrencyAmount from this ontology to simplify imports in cases where the broader definitions for commodities are not required.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220201/ProductsAndServices/ProductsAndServices.rdf version of this ontology was revised to eliminate deprecated elements related to precious metals.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/ProductsAndServices/ProductsAndServices.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to replace concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to replace additional concepts from several FIBO FND ontologies with their counterparts added to the Commons Ontology Library (Commons) v1.1.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20240101/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to replace the definition of real estate with the new definition in the real property ontology (LOAN-168).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20241001/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to simplify the agreements class hierarchy (FND-391).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250501/ProductsAndServices/ProductsAndServices.rdf version of the ontology was modified to eliminate long-deprecated content (FND-399) and to reuse concepts from the Commons 1.3 sites and facilities ontology (FND-401).
- **copyright**: Copyright (c) 2013-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
