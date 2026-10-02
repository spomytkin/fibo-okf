---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offering
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: expression of interest in providing something to someone that is contingent upon acceptance, forbearance, or some
      other consideration, as might be desired by an offeree(s)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The making of an offer is the first of three steps in the traditional process of forming a valid contract: an
      offer, an acceptance of the offer, and an exchange of consideration. (Consideration is the act of doing something or
      promising to do something that a person is not legally required to do, or the forbearance or the promise to forbear
      from doing something that he or she has the legal right to do.)'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: An offering may or may not be considered a 'state of affairs' or situation, depending on the circumstances. In
      some cases such as a prospectus or other offering in the context of financial services, an offering may also be classified
      as a situation. Users may choose to model an individual offering as both an offering and situation, depending on the
      circumstances, in other words.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offeree
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: offering
type: Ontology Class
---

# offering

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Offering>

## Definition

expression of interest in providing something to someone that is contingent upon acceptance, forbearance, or some other consideration, as might be desired by an offeree(s)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [Offeror](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: min qualified cardinality 0 of type [Offeree](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offeree.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Offeror](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/Offeror.md)

## Annotations

- **label**: offering
- **definition**: expression of interest in providing something to someone that is contingent upon acceptance, forbearance, or some other consideration, as might be desired by an offeree(s)
- **explanatoryNote**: The making of an offer is the first of three steps in the traditional process of forming a valid contract: an offer, an acceptance of the offer, and an exchange of consideration. (Consideration is the act of doing something or promising to do something that a person is not legally required to do, or the forbearance or the promise to forbear from doing something that he or she has the legal right to do.)
- **usageNote**: An offering may or may not be considered a 'state of affairs' or situation, depending on the circumstances. In some cases such as a prospectus or other offering in the context of financial services, an offering may also be classified as a situation. Users may choose to model an individual offering as both an offering and situation, depending on the circumstances, in other words.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
