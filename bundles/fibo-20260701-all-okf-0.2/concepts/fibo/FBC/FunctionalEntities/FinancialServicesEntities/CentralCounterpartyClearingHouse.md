---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: central counterparty clearing house
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: clearing house that helps facilitate trading in derivatives and equities markets
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CCP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'These clearing houses are often operated by the major banks in the country. The house''s prime responsibility
      is to provide efficiency and stability to the financial markets that they operate in.


      There are two main processes that are carried out by CCPs: clearing and settlement of market transactions. Clearing
      relates to identifying the obligations of both parties on either side of a transaction. Settlement occurs when the final
      transfer of securities and funds occur.


      CCPs benefit both parties in a transaction because they bear most of the credit risk. If two individuals deal with one
      another, the buyer bears the credit risk of the seller, and vice versa. When a CCP is used the credit risk that is held
      against both buyer and seller is coming from the CCP, which in all likelihood is much less than in the previous situation.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.esma.europa.eu/sites/default/files/EACH2.pdf
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralCounterpartyClearingHouse
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: central counterparty clearing house
type: Ontology Class
---

# central counterparty clearing house

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/CentralCounterpartyClearingHouse>

## Definition

clearing house that helps facilitate trading in derivatives and equities markets

## Relationships

- **See also**: [EACH2.pdf](<https://www.esma.europa.eu/sites/default/files/EACH2.pdf>)
- **Subclass of**: [ClearingHouse](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md)

## Annotations

- **label**: central counterparty clearing house
- **definition**: clearing house that helps facilitate trading in derivatives and equities markets
- **abbreviation**: CCP
- **explanatoryNote**: These clearing houses are often operated by the major banks in the country. The house's prime responsibility is to provide efficiency and stability to the financial markets that they operate in.  There are two main processes that are carried out by CCPs: clearing and settlement of market transactions. Clearing relates to identifying the obligations of both parties on either side of a transaction. Settlement occurs when the final transfer of securities and funds occur.  CCPs benefit both parties in a transaction because they bear most of the credit risk. If two individuals deal with one another, the buyer bears the credit risk of the seller, and vice versa. When a CCP is used the credit risk that is held against both buyer and seller is coming from the CCP, which in all likelihood is much less than in the previous situation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
